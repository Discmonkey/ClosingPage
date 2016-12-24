var ClosingPage = angular.module('ClosingPage', ['ui.router']);


ClosingPage.config(function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/choose-template');

    $stateProvider

        .state('choose-template', {
            url: '/choose-template',
            templateUrl: '/partials/choose-template.pug',
        })

        .state('template-one', {
            url: '/template-one',
            templateUrl: '/partials/template-one.pug'
        })

        .state('template-two', {
            url: '/template-two',
            templateUrl: 'partials/template-two.pug'
        });
});