'use strict';


// Declare app level module which depends on filters, and services
angular.module('iplui', ['iplui.filters', 'iplui.services', 'iplui.directives', 'iplui.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/view1', {templateUrl: 'partials/teamStats.html', controller: 'TeamStatsController'});
    $routeProvider.when('/view2', {templateUrl: 'partials/partial2.html', controller: 'MyCtrl2'});
    $routeProvider.otherwise({redirectTo: '/view1'});
  }]);
