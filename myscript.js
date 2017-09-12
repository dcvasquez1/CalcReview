$(document).ready(function() {
   $("#1").click(function() {
       $(".question").hide();
       $(".answer").hide();
       $("#nextButton").hide();
       $("#q1").show();
   })
   $("#2").click(function() {
       $(".question").hide();
       $(".answer").hide();
       $("#nextButton").hide();
       $("#q2").show();
   })
   $("#3").click(function() {
       $(".question").hide();
       $(".answer").hide();
       $("#nextButton").hide();
       $("#q3").show();
   })
   $("#4").click(function() {
       $(".question").hide();
       $(".answer").hide();
       $("#nextButton").hide();
       $("#q4").show();
   })
    $("#q1").click(function() {
        $("#a1").fadeIn();
        setTimeout(doNothing, 1000);
   })
    $("#q2").click(function() {
        $("#a2").fadeIn();
        setTimeout(doNothing, 1000);
   })
    $("#q3").click(function() {
        $("#a3").fadeIn();
        setTimeout(doNothing, 1000);
   })
    $("#q4").click(function() {
        $("#a4").fadeIn();
        setTimeout(doNothing, 1000);
   })
    $("#nextButton").click(function() {
       $(".question").fadeOut();
        $(".answer").fadeOut();
        $("#nextButton").fadeOut();
   })
})
function doNothing () {
    $("#nextButton").fadeIn();
}