function Preview($scope, $http) {
    $scope.showUpload = false;
    $scope.showPublish = true;

    if (window.templateId == undefined)
        var templateId = 0;

    $scope.publish = function() {
        console.log('clicked');
        $http({
            method: 'POST',
            url: '/publish-direct/'+templateId
        }).then(function(response) {
            console.log(response);
            var url = response.data['url'];
            swal({
                title: "<h2> Awesome! Your page has been published</h2>",
                text: "<p id='url-p'>" + url +"</p><button class='btn btn-success copy-button' " +
                "data-clipboard-action='copy' data-clipboard-target='#url-p'> Copy </button>",
                html: true
            });

        });
    };

    new Clipboard('.copy-button');
}