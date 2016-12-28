/**
 * Created by maxg on 12/26/16.
 */
var FileUpload = {
    templateUrl: '/partials/file-upload.pug',
    controller: function($http) {
        var self = this;
        this.showForm = true;
        this.showUploadForm = false;
        this.showLoading = false;
        this.showPPT = false;
        this.showGIF = false;
        this.showPDF = false;


        this.action = 'Power Point';
        this.dataSources = {
            pptData: [],
            gifSource: '',
            pdfSource: ''
        };

        this.showModal = function() {
            self.showForm = false;
            self.showUploadForm = true;
        };

        this.exitModal = function() {
            self.showUploadForm = false;
            self.showForm = true;
        };

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