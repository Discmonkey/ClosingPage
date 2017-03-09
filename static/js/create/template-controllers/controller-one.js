function TemplateOneCtrl($scope, $http, Template, $window) {
    var self = this;
    $scope.showUpload = true;
    $scope.showPublish = true;
    $scope.imageUploaded = false;
    $scope.logoUploaded = false;
    this.data = {
        uploads: {
            coverImage: {display: 'default', source:'//:0', name: ''},
            lrgDisplay: {display: 'default', source:'', name: ''},
            medDisplayLeft: {display: 'default', source:'', name: ''},
            medDisplayRight: {display: 'default', source:'', name: ''},
            logo: {display: 'default', source: '//:0', name: ''}
        },
        inputs: {
            'Subject': 'name',
            'Template Title': 'Template Title',
            'Main Description': 'Pitch',
            'Center Display Description': 'Description',
            'Left Display Description': 'Description',
            'Right Display Description': 'Description',
            'Quote': 'Awesome Quote'
        },
        footer: {
            signature: '',
            phone: '',
            calendly: '',
            email: ''
        }
    };

    this.popovers = {
        phone: false,
        email: false,
        calendly: false
    };

    $scope.inputs = this.data.inputs;
    $scope.uploads = this.data.uploads;
    $scope.footer = this.data.footer;
    $scope.popovers = this.popovers;

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

    $scope.preview = function() {
        Template.preview(self.data, 1).then(function(data) {
            if (data.data) {
                var location = "/preview/" + data.data.template_id;
                $window.location.href = location;
            }
        })
    };

    $scope.publish = function() {
        console.log('clicked');

        $http.post('/publish-from-create', self.data, {
            headers: {'Content-Type': 'application/json'}
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

    $scope.setFooter = function (signature, phone, calendly, email){
        self.data.footer.signature = signature;
        self.data.footer.phone = phone;
        self.data.footer.calendly = calendly;
        self.data.footer.email = email;
    };

    $scope.togglePopover = function (popover){
        for (var k in self.popovers) {
            if (self.popovers.hasOwnProperty(k) && k != popover)
                self.popovers[k] = false;
        }
        self.popovers[popover] = !self.popovers[popover];
    };

    new Clipboard('.copy-button');



}