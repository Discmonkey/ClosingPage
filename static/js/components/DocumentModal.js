/**
 * Created by jacob on 2/26/17.
 */
function DocumentModal(template, options) {
    if (options === undefined)
        options = {};

    return {
        template: template + '<div id="document-modal-close" class="btn btn-default" ng-click="$modal.close()"><i class="fa fa-times"></i></div>',
        controller: function ($uibModalInstance){
            var $ctrl = this;
            $.extend($ctrl, options);

            $ctrl.close = function (){
                $uibModalInstance.close({$value: null});
                $(document).off('click', '.document-modal .modal-dialog');
                $(document).off('click', '.document-modal .modal-content');
            };

            // hack to allow closing the modal because my CSS breaks it
            $(document).on('click', '.document-modal .modal-dialog', function () {
                $ctrl.close();
            });

            $(document).on('click', '.document-modal .modal-content', function (e) {
                e.stopPropagation();
            });
        },
        controllerAs: '$modal',
        windowClass: 'document-modal'
    };
}