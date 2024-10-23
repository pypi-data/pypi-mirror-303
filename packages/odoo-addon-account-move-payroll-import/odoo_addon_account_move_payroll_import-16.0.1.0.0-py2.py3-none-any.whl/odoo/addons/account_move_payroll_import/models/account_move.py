from collections import defaultdict
from contextlib import contextmanager

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    @contextmanager
    def _sync_dynamic_line(  # noqa: C901
        self,
        existing_key_fname,
        needed_vals_fname,
        needed_dirty_fname,
        line_type,
        container,
    ):
        """
        Overwrite this method to prevent line modifications in payroll import context
        See account/account_move.py for the original method.
        """
        def existing():
            return {
                line: line[existing_key_fname]
                for line in container["records"].line_ids
                if line[existing_key_fname]
            }

        def needed():
            res = {}
            for computed_needed in container["records"].mapped(needed_vals_fname):
                if computed_needed is False:
                    continue  # there was an invalidation, let's hope nothing needed to be changed...
                for key, values in computed_needed.items():
                    if key not in res:
                        res[key] = dict(values)
                    else:
                        ignore = True
                        for fname in res[key]:
                            if (
                                self.env["account.move.line"]._fields[fname].type
                                == "monetary"
                            ):
                                res[key][fname] += values[fname]
                                if res[key][fname]:
                                    ignore = False
                        if ignore:
                            del res[key]

            # Convert float values to their "ORM cache" one to prevent different rounding calculations
            for dict_key in res:
                move_id = dict_key.get("move_id")
                if not move_id:
                    continue
                record = self.env["account.move"].browse(move_id)
                for fname, current_value in res[dict_key].items():
                    field = self.env["account.move.line"]._fields[fname]
                    if isinstance(current_value, float):
                        new_value = field.convert_to_cache(current_value, record)
                        res[dict_key][fname] = new_value

            return res

        def dirty():
            *path, dirty_fname = needed_dirty_fname.split(".")
            eligible_recs = container["records"].mapped(".".join(path))
            if eligible_recs._name == "account.move.line":
                eligible_recs = eligible_recs.filtered(
                    lambda l: l.display_type != "cogs"
                )
            dirty_recs = eligible_recs.filtered(dirty_fname)
            return dirty_recs, dirty_fname

        # don't do anything if we are in a payroll import context
        if self.env.context.get("is_payroll_import"):
            yield
            return

        inv_existing_before = existing()
        needed_before = needed()
        dirty_recs_before, dirty_fname = dirty()
        dirty_recs_before[dirty_fname] = False
        yield
        dirty_recs_after, dirty_fname = dirty()
        if dirty_recs_before and not dirty_recs_after:  # TODO improve filter
            return
        inv_existing_after = existing()
        needed_after = needed()

        # Filter out deleted lines from `needed_before` to not recompute lines if not necessary or wanted
        line_ids = set(
            self.env["account.move.line"]
            .browse(k["id"] for k in needed_before if "id" in k)
            .exists()
            .ids
        )
        needed_before = {
            k: v
            for k, v in needed_before.items()
            if "id" not in k or k["id"] in line_ids
        }

        # old key to new key for the same line
        before2after = {
            before: inv_existing_after[bline]
            for bline, before in inv_existing_before.items()
            if bline in inv_existing_after
        }

        if needed_after == needed_before:
            return

        existing_after = defaultdict(list)
        for k, v in inv_existing_after.items():
            existing_after[v].append(k)
        to_delete = [
            line.id
            for line, key in inv_existing_before.items()
            if key not in needed_after
            and key in existing_after
            and before2after[key] not in needed_after
        ]
        to_delete_set = set(to_delete)
        to_delete.extend(
            line.id
            for line, key in inv_existing_after.items()
            if key not in needed_after and line.id not in to_delete_set
        )
        to_create = {
            key: values
            for key, values in needed_after.items()
            if key not in existing_after
        }
        to_write = {
            line: values
            for key, values in needed_after.items()
            for line in existing_after[key]
            if any(
                self.env["account.move.line"]
                ._fields[fname]
                .convert_to_write(line[fname], self)
                != values[fname]
                for fname in values
            )
        }

        while to_delete and to_create:
            key, values = to_create.popitem()
            line_id = to_delete.pop()
            self.env["account.move.line"].browse(line_id).write(
                {**key, **values, "display_type": line_type}
            )
        if to_delete:
            self.env["account.move.line"].browse(to_delete).with_context(
                dynamic_unlink=True
            ).unlink()
        if to_create:
            self.env["account.move.line"].create(
                [
                    {**key, **values, "display_type": line_type}
                    for key, values in to_create.items()
                ]
            )
        if to_write:
            for line, values in to_write.items():
                line.write(values)
