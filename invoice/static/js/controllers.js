function jobCtrl($scope, $rootScope, jobService) {



    $scope.getResourceObject = function() {
        var job = jobService.get({},
            function(data) {
                $scope.jobs = data.objects[0];

            }
        );
        return job.$promise;
    };

    $scope.getResourceObject();

}
