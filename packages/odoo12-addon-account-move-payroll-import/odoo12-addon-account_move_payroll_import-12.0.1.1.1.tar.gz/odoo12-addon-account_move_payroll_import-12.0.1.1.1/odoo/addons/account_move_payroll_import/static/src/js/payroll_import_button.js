odoo.define('account_move_payroll_import.payroll_import_button', function (require) {
    "use strict";

    var core = require('web.core');
    var _t = core._t;
    var ListController = require('web.ListController');

    const ResModel = 'payroll.import.wizard';

    ListController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);

            if (this.$buttons) {
                this.$buttons.find('.o_button_import_payroll').click(
                    this.proxy('payrollImportWizard')
                );
            }
        },
        payrollImportWizard: function () {
            this.do_action({
                name: _t('Import Payroll Wizard'),
                type: 'ir.actions.act_window',
                res_model: ResModel,
                views: [[false, 'form']],
                target: 'new',
            });
        }
    });
});