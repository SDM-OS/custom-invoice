angular.module("invoice", ["ui.bootstrap",  "ngCookies"]);




function MasterCtrl(t, e) {
    var o = 992;
    t.getWidth = function() {
        return window.innerWidth
    }, t.$watch(t.getWidth, function(g) {
        t.toggle = g >= o ? angular.isDefined(e.get("toggle")) ? e.get("toggle") ? !0 : !1 : !0 : !1
    }), t.toggleSidebar = function() {
        t.toggle = !t.toggle, e.put("toggle", t.toggle)
    }, window.onresize = function() {
        t.$apply()
    }
}
angular.module("invoice").controller("MasterCtrl", ["$scope", "$cookieStore", MasterCtrl]);