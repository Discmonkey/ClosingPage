/**
 * Created by jacob on 2/26/17.
 */
function DocumentModal(options){
    if (options === undefined)
        options = {};

    return function ($uibModalInstance){
        var $ctrl = this;
        $.extend($ctrl, options);

        // hack to allow closing the modal because my CSS breaks it
        $(document).on('click', '.document-modal .modal-dialog', function(){
            $uibModalInstance.close({$value: null});
            $(document).off('click', '.document-modal .modal-dialog');
            $(document).off('click', '.document-modal .modal-content');
        });

        $(document).on('click', '.document-modal .modal-content', function (e){
            e.stopPropagation();
        });
    };
}