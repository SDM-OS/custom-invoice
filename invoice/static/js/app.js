
var invoice = angular.module("invoice", ["invoiceServices"]).config(function(
            $interpolateProvider, $httpProvider) {

    
    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");
    

    $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
});
