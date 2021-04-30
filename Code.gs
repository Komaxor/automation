function SendForm() {
  let cast_sheet_id = getSheetId("top-cast");
  let email_sheet_id = getSheetId("emails");

  let formURL = createForm(cast_sheet_id);

  sendEmail(formURL, email_sheet_id);
}

function getSheetId(filename) {
  return DriveApp.getFilesByName(filename).next().getId();
}

function createForm(cast_sheet_id) {
  try {
    DriveApp.getFilesByName("Best Actors of the Week").next().getId();
  } catch (err) {
    Logger.log("Error");
  }

  let cast = Sheets.Spreadsheets.Values.get(cast_sheet_id, "A1:A").values;

  let cast_form = FormApp.create("Best Actors of the Week");
  cast_form
    .addMultipleChoiceItem()
    .setTitle("Who is your favorite actor?")
    .setChoiceValues(cast)
    .showOtherOption(false);
  return {
    puburl: cast_form.getPublishedUrl(),
    editurl: cast_form.getEditUrl(),
  };
}

function sendEmail(formURL, email_sheet_id) {
  let emails = Sheets.Spreadsheets.Values.get(email_sheet_id, "A1:A");
  let subject = "Vote NOW!";
  let body =
    "The form is ready, you can access it here " +
    formURL["puburl"] +
    " (published URL) and edit it here " +
    formURL["editurl"] +
    " (edit URL).";
  for (let counter = 0; counter < emails.values.length; counter++) {
    let recipient = String(emails.values[counter]);
    Logger.log("Sending email to: " + recipient);
    MailApp.sendEmail(
      (recipient = recipient),
      (subject = subject),
      (body = body)
    );
  }
}
