const showAnim = gsap.from(".svg-logo", {
    width: 100,
    height: 30,
    paused: true,
    duration: 0.2
}).progress(1);

ScrollTrigger.create({
    start: "top top",
    end: 99999,
    onUpdate: (self) => {
        self.direction === -1 ? showAnim.play() : showAnim.reverse()
    }
});

var messages = $('.toast')

$('.toast').toast('show')

$(function() {
    var nav = $("#main-nav .nav-item a")
    for (let i = 0; i < nav.length; i++) {
        if ($(nav[i]).attr("href") == location.pathname) {
            $(nav[i]).addClass('active').append("<span class=\"sr-only\">(current)</span>");
        }
    }
});

var suppressMsg

if (!document.cookie.includes("dismissed_msg=true") && !suppressMsg) {
    gsap.to(".msg-bar", { duration: .5, autoAlpha: 1 });
}

$(".msg-close").on("click", function() {
    gsap.to(".msg-bar", { duration: .5, autoAlpha: 0 });
    var cookie_exp = new Date();
    cookie_exp.setDate(cookie_exp.getDate() + 1)
    document.cookie = "dismissed_msg=true; expires=" + cookie_exp + "; path=/"
});