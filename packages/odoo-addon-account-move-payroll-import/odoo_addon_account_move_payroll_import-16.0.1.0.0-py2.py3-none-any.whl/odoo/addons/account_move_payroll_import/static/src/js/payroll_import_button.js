/** @odoo-module */

import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { ListController } from "@web/views/list/list_controller";


const ResModel = 'payroll.import.wizard';


export class AccountMovePayrollImportController extends ListController {
    setup() {
        super.setup();
    }

    OnPayrollImportClick() {
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            name: this.env._t('Import Payroll Wizard'),
            res_model: ResModel,
            views: [[false, 'form']],
            target: 'new',
        });
    }
}


registry.category("views").add("payroll_import_button_in_tree", {
    ...listView,
    Controller: AccountMovePayrollImportController,
    buttonTemplate: "account_move_payroll_import.ListView.Buttons",
});
