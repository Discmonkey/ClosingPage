function TemplateOneCtrl($scope) {
    $scope.uploads = {
        coverImage: false,
        lrgDisplay: false,
        medDisplayLeft: false,
        medDisplayRight: false
    };

    $scope.title = 'Title';
    $scope.description = 'Pitch';
    $scope.lrgDisplayDesc = 'Main Display Information';
    $scope.medDisplayLeft = 'Left Display Information';
    $scope.medDisplayRight = 'Right Display Information';

    $scope.mainQuote = 'Place your message here';

    $scope.inputs = {
        'Template Title': 'Title',
        'Main Description': 'Pitch',
        'Center Display Description': 'Description',
        'Left Display Description': 'Description',
        'Right Display Description': 'Description',
        'Quote': 'Awesome Quote'
    };
}