
function headerbg(){
  var scroll = $(window).scrollTop();  
   if (scroll >= 50) {
    $("header").addClass("header-bg");
   } 
   else {
     $("header").removeClass("header-bg");
    }
   }

 
$(window).scroll(function() {    
     headerbg();
});/* =========scroll End========= */ 


/* =========Ready Start========= */
$(document).ready(function(){
	  $("#menuShow").on('click', function(e){
		$('#menubox').toggleClass('menu-slide');
	  });
	  $("#menuClose").on('click', function(e){
		$('#menubox').toggleClass('menu-slide');
	  });
	  
$('.skillbar').each(function(){
		$(this).find('.skillbar-bar').animate({
			width:$(this).attr('data-percent')
		},6000);
	});
	
});/* =========Ready End========= */ 

/* ============Scroll Effect=============== */

var lastId,
    topMenu = $(".nav-menu-list"),
    topMenuHeight = topMenu.outerHeight(),
    // All list items
    menuItems = topMenu.find("a"),
    // Anchors corresponding to menu items
    scrollItems = menuItems.map(function(){
      var item = $($(this).attr("href"));
      if (item.length) { return item; }
    });
	var headHeight=$("header").height();
	
// Bind click handler to menu items
// so we can get a fancy scroll animation
menuItems.click(function(e){
  var href = $(this).attr("href"),
      offsetTop = href === "#" ? 0 : $(href).offset().top - headHeight;
  $('html, body').stop().animate({ 
      scrollTop: offsetTop
  },1000);
  e.preventDefault();
  $(this).parent("li").addClass("active").siblings().removeClass("active");

});

// Bind to scroll
$(window).scroll(function(){
   // Get container scroll position
   var fromTop = $(this).scrollTop()+topMenuHeight;
   
   // Get id of current scroll item
   var cur = scrollItems.map(function(){
     if ($(this).offset().top < fromTop)
       return this;
   });
   // Get the id of the current element
   cur = cur[cur.length-1];
   var id = cur && cur.length ? cur[0].id : "";
   
  /* if (lastId !== id) {
       lastId = id;
       // Set/remove active class
       menuItems
         .parent().removeClass("active")
         .end().filter("[href='#"+id+"']").parent().addClass("active");
   }*/                   
});

/* ============Scroll Effect END=============== */
