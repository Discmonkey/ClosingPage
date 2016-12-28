function TemplateTwoCtrl($scope) {
    $scope.uploads = {
        coverImage: false,
        medDisplayLeft: false,
        medDisplayRight: false,
        smlDisplayLeft: false,
        smlDisplayMid: false,
        smlDisplayRight: false
    };

    $scope.title = 'Title';
    $scope.lrgDisplayDesc = 'Main Display Information';
    $scope.medDisplayLeft = 'Left Display Information';
    $scope.medDisplayRight = 'Right Display Information';

    $scope.mainQuote = 'Place your message here';

    $scope.inputs = {
        'Template Title': 'Title',
        'Main Description': 'Pitch',
        'Left Display Description': 'Description',
        'Right Display Description': 'Description',
        'Left Small Description': 'Description',
        'Middle Small Description': 'Description',
        'Right Small Description': 'Description',
        'Quote': 'Awesome Quote'
    };

}