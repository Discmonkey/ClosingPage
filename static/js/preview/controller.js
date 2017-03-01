function Preview($scope, $http, $uibModal) {
    $scope.showUpload = false;
    $scope.showPublish = true;

    $scope.publish = function() {
        $http({
            method: 'POST',
            url: '/publish-direct/'+ (templateId | 0 )
        }).then(function(response) {
            var url = response.data['url'];
            swal({
                title: "<h2> Awesome! Your page has been published</h2>",
                text: "<p id='url-p'>" + url +"</p><button class='btn btn-success copy-button' " +
                "data-clipboard-action='copy' data-clipboard-target='#url-p'> Copy </button>",
                html: true
            });

        });
    };

    $scope.showImageModal = function(path) {
        $uibModal.open({
            template: '<img ng-src="{($modal.path)}">',
            controller: DocumentModal({path: path}),
            controllerAs: '$modal',
            windowClass: 'document-modal'
        });
    };

    new Clipboard('.copy-button');
}