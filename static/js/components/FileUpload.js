/**
 * Created by maxg on 12/26/16.
 */
var FileUpload = {
    bindings: {
        state: '='
    },
    templateUrl: '/partials/file-upload.pug',
    controller: function($http) {
        var self = this;
        self.state.display = 'default';
        this.showModal = function() {
            self.state.display = 'form';
        };

        this.exitModal = function() {
            self.state.display = 'default'
        };

        this.sources = {
            gif: '//:0',
            ppt: [],
            pdf: '//:0'
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
                self.sources[data.display] = data.source;
            },function(data) {
                console.log(data);
            });
        };
    }
};