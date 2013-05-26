'use strict';

/* Controllers */

angular.module('iplui.controllers', ['ngResource'])


function TeamStatsController($scope, $resource) {
    var serverUrl = 'http://localhost:8888\:8888/:action';

    $scope.iplResource = $resource(serverUrl,
        {action: 'players', callbacks: 'JSON_CALLBACK'},
        {get: {method: 'JSONP'}});

    $scope.playerStats = $scope.iplResource.get();
}

function MyCtrl2() {

}

//TeamStatsController.$inject = ['$scope', '$resource']