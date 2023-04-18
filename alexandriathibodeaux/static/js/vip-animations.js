gsap.registerPlugin(ScrollTrigger);
gsap.registerPlugin(ScrollToPlugin);

let playOptions = "restart complete complete reset";
let startString = "top 90%";
let jerk = gsap.utils.wrap(["12%", "-12%"]);
let tilt = gsap.utils.wrap(["5", "-10", "-12", "6"]);

// Scroll arrow animations
// gsap.to(".scroll-arrow", { y: 8, ease: "power1.inOut", repeat: -1, yoyo: true });

// $("#scrollReminder").on("click", function () {
//     gsap.to(window, { duration: .75, scrollTo: ".who-iam" });
// });

// A to B line
gsap.timeline({
    scrollTrigger: {
        trigger: ".vip-landing .hero-diagram",
        toggleActions: "play complete complete complete",
    }
})
    .from("#a-pin", {
        opacity: 0,
        y:-100,
        duration: .75,
        ease: "back.out(1.7)",
    })
    .from(".vip-landing .hero-diagram .dotted-line", {
        scaleX: 0,
        duration: 1.25,
        ease: "power4.out",
    }, ">-0.25")
    .from("#b-pin", {
        opacity: 0,
        y:-100,
        duration: .75,
        ease: "back.out(1.7)",
    }, ">-0.75")
    .from(".sub-heading.author", {
        opacity: 0,
        y: -50,
        ease: "back.out(1.7)",
    })
    .from(".hero-cta", {
        opacity: 0,
        y: -50,
        ease: "back.out(1.7)",
    })

// Who I am Animation
gsap.timeline({
    scrollTrigger: {
        trigger: ".who-iam ul",
        toggleActions: playOptions,
        start: startString,
        end: "bottom top",
        // markers: true,
    }
})
    .from(".who-iam ul li", {
        opacity: 0,
        y: -50,
        ease: "back.out(1.7)",
        stagger: 0.5,
    })
    .from(".who-iam-cta", {
        opacity: 0,
        y: -50,
        ease: "back.out(1.7)",
        stagger: 0.75
    })
    .from(".who-iam-cta span", {
        opacity: 0,
        y: 50,
        ease: "back.out(1.7)",
        stagger: 0.75
    })

// Middle Part Animation
gsap.timeline({
    scrollTrigger: {
        trigger: ".middle-part ul",
        toggleActions: playOptions,
        start: startString,
        end: "bottom top",
        // markers: true,
    }
})
    .from(".middle-part ul li", {
        x: jerk,
        opacity: .25,
        duration: .1,
        stagger: .5,
        ease: "back.out"
    })
    .from(".middle-part-cta", {
        y: 50,
        opacity: 0,
        ease: "back.out",
        duration: .2
    }, ">.5")

// Insta Quote Animation
gsap.timeline({
    scrollTrigger: {
        trigger: ".instagram-love",
        toggleActions: playOptions,
        start: "top 80%",
        end: "bottom top",
        // markers: true,
    }
})
    .from(".insta-quote", {
        duration: 1,
        scale: 0,
        ease: "power1.inOut",
        stagger: {
            from: "center",
            amount: .25,
        }
    })
    .from(".quote-left-icon", {
        duration: 1.5,
        x: "10%",
        ease: "power1.inOut",
        yoyo: true,
        repeat: -1,
    }, "<")
    .from(".quote-right-icon", {
        duration: 1.5,
        x: "-10%",
        ease: "power1.inOut",
        yoyo: true,
        repeat: -1,
    }, "<")