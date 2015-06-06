angular.module("invoiceServices", ["ngResource"])

    .config(function($httpProvider) {
        $httpProvider.defaults.headers.post["Content-Type"] = "application/json;";
    })
    