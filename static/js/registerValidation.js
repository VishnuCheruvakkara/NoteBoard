document.addEventListener('DOMContentLoaded', function () {
  const validation = new JustValidate('#registerForm', {
    validateBeforeSubmitting: true,
  });

  validation
    .addField('#id_username', [
      { rule: 'required', errorMessage: 'Username is required' },
      { rule: 'minLength', value: 3, errorMessage: 'At least 3 characters' },
    ])
    .addField('#id_email', [
      { rule: 'required', errorMessage: 'Email is required' },
      { rule: 'email', errorMessage: 'Invalid email address' },
    ])
    .addField('#id_password1', [
      { rule: 'required', errorMessage: 'Password is required' },
      { rule: 'password', errorMessage: 'Password is too weak' },
    ])
    .addField('#id_password2', [
      { rule: 'required', errorMessage: 'Please confirm your password' },
      {
        validator: (value, fields) =>
          value === fields['#id_password1'].elem.value,
        errorMessage: 'Passwords do not match',
      },
    ])
    .onSuccess((event) => {
      event.target.submit(); // normal Django form submission
    });
});
