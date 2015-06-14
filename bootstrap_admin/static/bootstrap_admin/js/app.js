'use strict';

/**
 * @ngdoc overview
 * @name marriageSettingsApp
 * @description
 * # marriageSettingsApp
 *
 * Main module of the application.
 */
angular
  .module('marriageSettingsApp', [
    'ngRoute',
    'smart-table',
    'ui.bootstrap'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: '' + static_url + 'views/main.html',
        controller: 'MainCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
