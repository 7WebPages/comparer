/* Project specific Javascript goes here. */

$(document).ready(function(){
  $(".dateinput").datepicker({autoclose: true, todayHighlight: true});
  $(".datetimeinput").datetimepicker({format: "YYYY-MM-DD H:m"});
})

try{
  setTimeout(function(){
    if($ && $.fn && $.fn.select2){
      $.fn.select2.defaults.allowClear = true;  
    }
  },
  300)
}catch(e){}
