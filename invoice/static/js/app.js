var invoice = angular.module("invoice", ["invoiceServices" ]).config(function(
            $interpolateProvider, $httpProvider) {

    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");
 
    $httpProvider.defaults.headers.common["X-CSRFToken"] = getCookie("csrftoken");
});
