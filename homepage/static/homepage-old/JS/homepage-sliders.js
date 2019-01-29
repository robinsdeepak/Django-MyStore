		var slideIndex = 1;
         showSlides(slideIndex);

         function plusSlides(n) {
           showSlides(slideIndex += n+2);
        }

        function showSlides(n) {
          var i,k;
          var slides = document.getElementsByClassName("mySlides");
          if (n > slides.length) {slideIndex = 1}
          if (n < 1) {slideIndex = slides.length}
          for (i = 0; i < slides.length; i++) {
             slides[i].style.display = "none";
          }
		  for(i=0;i<slides.length;i++){
                var NewSlides2=[slideIndex-1,slideIndex,slideIndex+1];

            for (k=0; k<3; k++)
                slides[NewSlides2[k]].style.display = "inline-block";
            }

       }
		 var slideIndex2 = 1;
         showSlides2(slideIndex2);

         function plusSlides2(q) {
           showSlides2(slideIndex2 += q+2);
        }

        function showSlides2(q) {
            var i;
            var slides2 = document.getElementsByClassName("mySlides2");
            if (q > slides2.length) {slideIndex2 = 1}
            if (q < 1) {slideIndex2 = slides2.length}
            for (i = 0; i < slides2.length; i++) {
             slides2[i].style.display = "none";
            }
            for(i=0;i<slides2.length;i++){
                var NewSlides3=[slideIndex2-1,slideIndex2,slideIndex2+1];

            for (k=0; k<3; k++)
                slides2[NewSlides3[k]].style.display = "inline-block";
            }

       }
		 var slideIndex3 = 1;
         showSlides3(slideIndex3);

         function plusSlides3(r) {
           showSlides3(slideIndex3 += r+2);
        }

        function showSlides3(r) {
          var i,k;
          var slides3 = document.getElementsByClassName("mySlides3");
          if (r > slides3.length) {slideIndex3 = 1}
          if (r < 1) {slideIndex3 = slides3.length}
          for (i = 0; i < slides3.length; i++) {
             slides3[i].style.display = "none";
          }
		  for(i=0;i<slides3.length;i++){
                var NewSlides2=[slideIndex3-1,slideIndex3,slideIndex3+1];

            for (k=0; k<3; k++)
                slides3[NewSlides2[k]].style.display = "inline-block";
            }

       }


	   var slideIndex4 = 1;
         showSlides4(slideIndex4);

         function plusSlides4(n) {
           showSlides4(slideIndex4 += n+5);
        }

        function showSlides4(n) {
          var i;
          var slides4 = document.getElementsByClassName("mySlides4");
          if (n > slides4.length) {slideIndex4 = 1}
          if (n < 1) {slideIndex4 = slides4.length}
          for (i = 0; i < slides4.length; i++) {
             slides4[i].style.display = "none";
          }
          for(i=0;i<slides4.length;i++){
                var NewSlides4=[slideIndex4-1,slideIndex4,slideIndex4+1,slideIndex4+2,slideIndex4+3,slideIndex4+4];

            for (k=0; k<6; k++)
                slides4[NewSlides4[k]].style.display = "inline-block";
            }
       }