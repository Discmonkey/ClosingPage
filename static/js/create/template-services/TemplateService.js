/**
 * Created by maxg on 1/8/17.
 */

function TemplateService($http) {

    this.saveTemplate = function(data, templateNum){
        return $http.post('/save-template/' + templateNum, data, {
            headers: {'Content-Type': 'application/json'}
        })
    };

    this.loadTemplate = function(templateNum){
        return $http.get('/load-template/' + templateNum)
    };

    this.preview = function(data, templateNum) {
        return $http.post('/preview/' + templateNum, data, {
            headers: {'Content-Type': 'application/json'}
        });
    }
}