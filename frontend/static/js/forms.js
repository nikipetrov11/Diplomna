(function ($) {
	
	"use strict";

	var $document = $(document),
		$window = $(window),
		forms = {
			contactForm: $('#contactform'),
			appointmentForm: $('#appointment-form') ,
      quoteForm: $('#quote-form')
		};

	$document.ready(function () {
   
    // quote form
		if (forms.quoteForm.length) {
			var $quoteForm = forms.quoteForm;
			$quoteForm.validate({
				rules: {
					name: {
						required: true,
						minlength: 2
					},
					message: {
						required: true,
						minlength: 20
					},
					email: {
						required: true,
						email: true
					}

				},
				messages: {
					name: {
						required: "Моля въведете вашето име",
						minlength: "Вашето име трябва да се състои от поне 2 знака"
					},
					message: {
						required: "Моля, въведете съобщение",
						minlength: "Вашето съобщение трябва да се състои от поне 20 знака"
					},
					email: {
						required: "Моля, въведете своя имейл"
					}
				},
				submitHandler: function (form) {
					$(form).ajaxSubmit({
						type: "POST",
						data: $(form).serialize(),
						url: "form/process-quote.php",
						success: function () {
							$('#successQuote').fadeIn();
							$('#quote-form').each(function () {
								this.reset();
							});
						},
						error: function () {
							$('#quote-form').fadeTo("slow", 0, function () {
								$('#errorQuote').fadeIn();
							});
						}
					});
				}
			});
		}
    
    
		// appointment form
		if (forms.appointmentForm.length) {
			var $appointmentForm = forms.appointmentForm;
			$appointmentForm.validate({
				rules: {
					name: {
						required: true,
						minlength: 2
					},
					message: {
						required: true,
						minlength: 20
					},
					email: {
						required: true,
						email: true
					}

				},
				messages: {
					name: {
						required: "Моля въведете вашето име",
						minlength: "Вашето име трябва да се състои от поне 2 знака"
					},
					message: {
						required: "Моля, въведете съобщение",
						minlength: "Вашето съобщение трябва да се състои от поне 20 знака"
					},
					email: {
						required: "Моля, въведете своя имейл"
					}
				},
				submitHandler: function (form) {
					$(form).ajaxSubmit({
						type: "POST",
						data: $(form).serialize(),
						url: "form/process-appointment.php",
						success: function () {
							$('#successAppointment').fadeIn();
							$('#appointment-form').each(function () {
								this.reset();
							});
						},
						error: function () {
							$('#appointment-form').fadeTo("slow", 0, function () {
								$('#errorAppointment').fadeIn();
							});
						}
					});
				}
			});
		}

		// contact page form
		if (forms.contactForm.length) {
			var $contactform = forms.contactForm;
			$contactform.validate({
				rules: {
					name: {
						required: true,
						minlength: 2
					},
					message: {
						required: true,
						minlength: 20
					},
					email: {
						required: true,
						email: true
					}

				},
				messages: {
					name: {
						required: "Моля въведете вашето име",
						minlength: "Вашето име трябва да се състои от поне 2 знака"
					},
					message: {
						required: "Моля, въведете съобщение",
						minlength: "Вашето съобщение трябва да се състои от поне 20 знака"
					},
					email: {
						required: "Моля, въведете своя имейл"
					}
				},
				submitHandler: function (form) {
					$(form).ajaxSubmit({
						type: "POST",
						data: $(form).serialize(),
						url: "form/process-contact.php",
						success: function () {
							$('#success').fadeIn();
							$('#contactform').each(function () {
								this.reset();
							});
						},
						error: function () {
							$('#contactform').fadeTo("slow", 0, function () {
								$('#error').fadeIn();
							});
						}
					});
				}
			});
		}
		// datepicker
			if ($('.datetimepicker').length) {
				$('.datetimepicker').datetimepicker({
					format: 'DD/MM/YYYY',
					icons: {
						time: 'icon icon-clock',
						date: 'icon icon-calendar',
						up: 'icon icon-arrow_up',
						down: 'icon icon-arrow_down',
						previous: 'icon icon-arrow-left',
						next: 'icon icon-arrow-right',
						today: 'icon icon-today',
						clear: 'icon icon-trash',
						close: 'icon icon-cancel-music'
					}
				});
			}
			if ($('.timepicker').length) {
				$('.timepicker').datetimepicker({
					format: 'LT',
					icons: {
						time: 'icon icon-clock',
						up: 'icon icon-arrow_up',
						down: 'icon icon-arrow_down',
						previous: 'icon icon-arrow-left',
						next: 'icon icon-arrow-right'
					}
				});
			}

	});
	
})(jQuery);