function TemplateOneCtrl($scope, $http, Template) {
    var self = this;
    $scope.showUpload = true;
    $scope.showPublish = true;
    $scope.imageUploaded = false;
    $scope.logoUploaded = false;
    this.data = {
        uploads: {
            coverImage: {display: 'default', source:'//:0'},
            lrgDisplay: {display: 'default', source:''},
            medDisplayLeft: {display: 'default', source:''},
            medDisplayRight: {display: 'default', source:''},
            logo: {display: 'default', source: '//:0'}
        },
        inputs: {
            'Subject': 'name',
            'Template Title': 'Template Title',
            'Main Description': 'Pitch',
            'Center Display Description': 'Description',
            'Left Display Description': 'Description',
            'Right Display Description': 'Description',
            'Quote': 'Awesome Quote'
        }
    };

    $scope.inputs = this.data.inputs;
    $scope.uploads = this.data.uploads;

    // $scope.$watch('uploads', function(newVal, oldVal){
    //     console.log('old', oldVal);
    //     console.log('new', newVal);
    // }, true);

    $scope.uploadJPG = function(files, target) {
        var fd = new FormData();
        fd.append("file", files[0]);
        $http.post('/upload', fd, {
            withCredentials: true,
            headers: {'Content-Type': undefined },
            transformRequest: angular.identity
        }).then(function(data){
            data = data.data;
            $scope.uploads[target].source = data.source;
            if(target == 'logo') {
                $scope.logoUploaded = true;
            } else {
                $scope.imageUploaded = false;
            }
        },function(data) {
            console.log(data);
        });
    };

    $scope.save = function() {
        Template.saveTemplate(self.data, 1).then(function(data) {
            swal('Saved!', 'Come back whenever to finish', 'success');
        });
    };



}