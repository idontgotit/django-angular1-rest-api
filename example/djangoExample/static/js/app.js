/**
 * Created by python on 17/05/2017.
 */
var app = angular.module('myApp', ['ngStorage']);
app.config(function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})

app.controller('RegisterController', function ($scope, $http, $localStorage) {

    function successFn() {
        console.log('true!');

    }

    function errorFn(data, status, headers, config) {
        console.error('Epic failure!');
    }

    $scope.register = function () {

        $http({
            method: 'POST',
            url: '/api/register/',
            data: {'username': $scope.username, 'password': $scope.password}
        }).then(successFn, errorFn);

    };

    $scope.myFunc = function (name) {
        // console.log('inside');
        //  console.log('username = ' + $scope.username);
        $http({
            method: 'GET',
            url: '/api/users/' + name,
        }).then(function (response) {
            $scope.show = true;
            $scope.resultUsername = response.data.username;
            $scope.resultPassword = response.data.password;
            $scope.resultId = response.data.id;
            $localStorage.userId = $scope.resultId;
        }, function (response) {
        });

        $http({
            method: 'GET',
            url: '/api/users/' + $localStorage.userId +"/posts",
        }).then(function (response) {
            console.log(response.data)
            $scope.allPosts = response.data;
        }, function (response) {
        });

    };

    $scope.saveNewPost = function () {
        $http({
            method: 'POST',
            url: '/api/posts',
            data: {'title': $scope.newPost.title, 'body': $scope.newPost.body, 'author_id': $localStorage.userId}
        })
    };


});


