angular.module("invoiceServices", ["ngResource"])

    .config(function($httpProvider) {
        $httpProvider.defaults.headers.post["Content-Type"] = "application/json;";
    })

    .factory("jobService", function($resource) {
        var url = "/api/v1/job/:id/",
            jobs = $resource(url, {
                id: "@id"
            }, {
                update: {
                    method: "PUT"
                },
     
            });

        return jobs;
    })