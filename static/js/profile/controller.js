/**
 * Created by jacob on 3/14/17.
 */
function Profile($http){
    var self = this;
    this.loading = false;
    this.pictureUrl = '';
    this.style = {'margin-top': 0, 'background-image': 'url(' + this.pictureUrl + ')'};

    this.setPicture = function (url){
        self.pictureUrl = url;
        self.style['background-image'] = 'url(' + self.pictureUrl + ')';
    };

    this.uploadPicture = function (files){
        var fd = new FormData();
        //Take the first selected file
        fd.append("file", files[0]);
        self.loading = true;
        $http.post('/upload', fd, {
            withCredentials: true,
            headers: {'Content-type': undefined}
        }).then(function (data){
            self.setPicture(data.data.source);
            self.loading = false;
        }, function (data){
            console.log(data);
            self.loading = false;
        });
    };
}