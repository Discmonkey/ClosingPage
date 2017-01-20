var PPTDisplay = {
    controller: function(){
        this.slideIndex = 0;

        this.left = function() {
            if(this.slideIndex > 0) {
                this.slideIndex -=1;
            }
        };

        this.right = function() {
            if(this.slideIndex < this.slides.length) {
                this.slideIndex += 1;
            }
        };


    },
    bindings: {
        slides: '='
    },
    templateUrl: '/partials/ppt-display.pug'
};