function TemplatePickerCtrl($scope, $state) {

    $scope.displayTempOne = true;
    $scope.controllerTest = 'Max';
    $scope.preview = function(bool) {
        if ($scope.displayTempOne != bool) {
            $scope.displayTempOne = bool;
            if (bool) {
                $state.go('choose-template.preview-one');
            } else {
                $state.go('choose-template.preview-two');
            }
        }
    }
}
