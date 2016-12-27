/**
 * Created by maxg on 12/26/16.
 */
var FileUpload = {
    templateUrl: [
        '<div class="form-component">',
            '<div class="presentation text-center">',
                '<img class="upload", ng-show="$ctrl.showForm", ' +
                'src="/static/img/phase-one/upload.svg", ng-click="$ctrl.showModal()">',
                '<div class="mini-modal text-center jumbotron", ng-show="$ctrl.showUploadForm">',
                    '<h5> Cool, lets go grab your files. </h5>',
                    '<label class="myLabel">',
                        '<button class="btn btn-success"> Upload </button>',
                        '<span> Upload </span>',
                    '</label>',
                '</div>',
            '</div>',
        '</div>'
    ].join(''),
    controller: function($http) {
        var self = this;
        this.showForm = true;
        this.showUploadForm = false;
        this.showLoading = false;
        this.showPPT = false;
        this.showGIF = false;
        this.showPDF = false;

        this.dataSources = {
            pptData: [],
            gifSource: '',
            pdfSource: ''
        };

        this.showModal = function() {
            self.showForm = false;
            self.showUploadForm = true;
        }

        this.uploadFile = function(files) {
            var fd = new FormData();
            //Take the first selected file
            fd.append("file", files[0]);
            this.showLoading = true;
            this.show
            $http.post(uploadUrl, fd, {
                withCredentials: true,
                headers: {'Content-Type': undefined },
                transformRequest: angular.identity
            }).success().error();

        };
    }
};