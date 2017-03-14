/**
 * Created by maxg on 12/26/16.
 */
var FileUpload = {
    bindings: {
        state: '='
    },
    templateUrl: '/angular-components/file-upload.pug',
    controller: function($http) {
        var self = this;
        self.state.display = 'default';
        self.state.name = '';
        this.showModal = function() {
            self.state.display = 'form';
        };

        this.exitModal = function() {
            self.state.display = 'default'
        };

        this.sources = {
            gif: '//:0',
            ppt: [],
            pdf: []
        };

        this.uploadFile = function(files) {
            var fd = new FormData();
            //Take the first selected file
            fd.append("file", files[0]);
            self.state.display = 'load';
            $http.post('/upload', fd, {
                withCredentials: true,
                headers: {'Content-Type': undefined },
                transformRequest: angular.identity
            }).then(function(data){
                data = data.data;
                self.state.source = data.source;
                self.state.display = data.display;
                self.state.name = data.name;
                self.sources[data.display] = data.source;
            },function(data) {
                console.log(data);
            });
        };

        this.deleteFile = function (){
            self.state.display = 'load';
            $http.post('/removeFile', {filename: self.state.name}, {
                withCredentials: true
            }).then(function (){
                self.state.display = 'form';
                self.state.source = '';
                self.sources.gif = '//:0';
                self.sources.ppt = [];
                self.sources.pdf = [];
            },function (data){
                console.log('Error:');
                console.log(data);
            });
        };
    }
};