function playPause() {
	if ($(".playPause").attr("name") == "play") {
		$(".playPause").css("background-position", "center bottom");
		$(".audioFile").get(0).play();
		$(".playPause").attr("name", "pause");
	}
	else {
		$(".playPause").css("background-position", "center top");
		$(".audioFile").get(0).pause();
		$(".playPause").attr("name", "play");
	}
}

$('.volumizer').on('change', function() {
	sliderVal = $(".volumizer").val();
	volumeVal = sliderVal/100;
	$(".audioFile").prop("volume", volumeVal);
	if (volumeVal > ".66") {
		$(".sound").css("background-position", "center bottom");
	}
	else if (volumeVal > ".33") {
		$(".sound").css("background-position", "center center");
	}
	else {
		$(".sound").css("background-position", "center top");
	}
});
$(".sound").click( function() {
	$(".soundDropup").toggle();
});

var duration = $(".audioFile").get(0).duration;
console.log(duration);

$(".song").click( function() {
	var songToChange = $(this).attr("name");
	$(".audioFile").attr("src", songToChange);
	$(".audioFile").attr("autoplay", "autoplay");
	
	var songName = $(this).attr("id");
	var artistName = $(this).find(".artistName").text();
	$(".playingSong").text(songName);
	$(".playingArtist").text(artistName);
	
	if ($(".playPause").attr("name") == "play") {
		$(".playPause").css("background-position", "center bottom");
		$(".audioFile").get(0).play();
		$(".playPause").attr("name", "pause");
	}
	else if ($(this).attr("name") == $(".audioFile").attr("src")) {
		$(".playPause").css("background-position", "center bottom");
		$(".audioFile").get(0).play();
		$(".playPause").attr("name", "pause");
	}
	else {
		$(".playPause").css("background-position", "center top");
		$(".audioFile").get(0).pause();
		$(".playPause").attr("name", "play");
	}
});

$(".uploadBtn").click( function() {
	$(".songUploadInput").click();
});

/* Upload button popup

This code has been retired for UX sake. It was beautiful, but we must move on ;( ;(

$(".uploadBtn").click( function() {
	$(".uploadPopup").toggle();
	$(".uploadBtn").text("Close");
	$(".uploadBtn").attr("style", "background-color: #ff412e; background-image: -webkit-gradient(linear, left top, left bottom, from(rgb(255, 65, 46)), to(rgb(212, 29, 0))); background-image: -webkit-linear-gradient(top, rgb(255, 65, 46), rgb(212, 29, 0)); background-image: -moz-linear-gradient(top, rgb(255, 65, 46), rgb(212, 29, 0)); background-image: -o-linear-gradient(top, rgb(255, 65, 46), rgb(212, 29, 0)); background-image: -ms-linear-gradient(top, rgb(255, 65, 46), rgb(212, 29, 0)); background-image: linear-gradient(top, rgb(255, 65, 46), rgb(212, 29, 0)); filter: progid:DXImageTransform.Microsoft.gradient(GradientType=0,StartColorStr='#ff412e', EndColorStr='#d41d00'); box-shadow: inset 0 1px #ff5843, 0 2px 4px black;");
	$(".uploadPopup").animate({
		opacity:1
	}, 200);
	$(".uploadPopupWindow").animate({
		opacity:1,
		margin: "-250px auto 0 -250px"
	}, 0);
});
*/

