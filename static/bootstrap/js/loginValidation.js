document.addEventListener("DOMContentLoaded", function () {
  const validation = new JustValidate("#loginForm");

  validation
    .addField("#id_username", [
      { rule: "required", errorMessage: "Email or username is required" },
    ])
    .addField("#id_password", [
      { rule: "required", errorMessage: "Password is required" },
    ])
    .onSuccess((event) => {
      const button = document.getElementById("loginBtn");
      button.disabled = true;
      button.textContent = "Logging in...";
      event.target.submit();
    });
});
