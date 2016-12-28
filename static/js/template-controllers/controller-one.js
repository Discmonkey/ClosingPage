function TemplateOneCtrl($scope) {
    $scope.uploads = {
        coverImage: false,
        lrgDisplay: false,
        medDisplayLeft: false,
        medDisplayRight: false
    };

    $scope.inputs = {
        'Template Title': 'Title',
        'Main Description': 'Pitch',
        'Center Display Description': 'Description',
        'Left Display Description': 'Description',
        'Right Display Description': 'Description',
        'Quote': 'Awesome Quote'
    };
}