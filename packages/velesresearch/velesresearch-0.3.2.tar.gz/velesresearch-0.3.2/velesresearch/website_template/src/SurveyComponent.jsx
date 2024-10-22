import { Model } from "survey-core";
import { Survey } from "survey-react-ui";
import "survey-core/survey.i18n";
import "survey-core/defaultV2.min.css";
import { json } from "./survey.js";
import * as SurveyCore from "survey-core";
import { nouislider } from "surveyjs-widgets";
import "nouislider/distribute/nouislider.css";
import { Converter } from "showdown";
import * as config from "./config.ts";
import CSRFToken from "./csrf.ts";
import registerCustomFunctions from "./customExpressionFunctions.js";

nouislider(SurveyCore);

function MakeID(length) {
  let result = "";
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  const charactersLength = characters.length;
  let counter = 0;
  while (counter < length) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
    counter += 1;
  }
  return result;
}

function groupNumber(max) {
  return Math.floor(Math.random() * max + 1);
}

function createResults(survey) {
  // Create results object
  if (!survey.getVariable("dateCompleted")) {
    const dateCompleted = new Date();
    survey.setVariable("dateCompleted", dateCompleted.toISOString());
  }

  const variables = {};
  for (const variable of survey.getVariableNames()) {
    if (survey?.calculatedValues.some( // Skip calculatedValues that are not included into results
      dict => (dict.name === variable || dict.name?.toLowerCase() === variable) && dict.includeIntoResult === false
    )) continue;
    variables[variable] = survey.getVariable(variable);
  }

  const URLparams = Object.fromEntries(new URLSearchParams(window.location.search));

  return Object.assign(
    {
      id: survey.participantID
    },
    survey.data,
    URLparams,
    variables
  );
}

async function handleResults(survey, completedHtml) {
  const result = createResults(survey);

  // Add scores to results
  if (survey.addScoreToResults === undefined || survey.addScoreToResults) {
    for (const question of survey.getAllQuestions()) {
      if (question.correctAnswer && question.selectedItem) {
        result[question.name + (survey.scoresSuffix || "_score")] = question.selectedItem.value === question.correctAnswer ? 1 : 0;
      }
    }
  }

  // Wait for reCAPTCHA to be ready and get token
  let siteKey = new URL(document.getElementById("recaptchaScript").src).searchParams.get("render");
  let recaptchaToken;
  if (siteKey) {
    await new Promise(resolve => window.grecaptcha.ready(resolve));
    recaptchaToken = await window.grecaptcha.execute(siteKey, { action: 'submit' });
  } else {
    recaptchaToken = NaN;
  }
  Object.assign(result, { "g-recaptcha-token": recaptchaToken });

  // send data to Django backend
  const requestHeaders = {
    method: "POST",
    headers: Object.assign(
      {
        "Content-Type": "application/json",
      },
      CSRFToken()
    ),
    body: JSON.stringify(result),
  };
  const url = window.location.pathname + "submit/";
  const response = await fetch(url, requestHeaders);

  if (response.ok) {
    document.getElementsByClassName("sd-completedpage")[0].innerHTML = completedHtml;
    document.getElementById("tryAgainDiv").style.display = "none";
    document.getElementById("tryAgainButton").disabled = true;
    return "OK";
  } else {
    document.getElementsByClassName("sd-completedpage")[0].innerHTML = `
        <div style="text-align: center">${SurveyCore.surveyLocalization.getString("savingDataError", survey.locale)}</div>
        <br>
        <div style="text-align: center; font-size: 3em; color: #CC0000; font-weight: bold">Error ${response.status}</div>
        <br>
        <div style="text-align: center; padding-bottom: 2em; font-size: 2em">${response.statusText}</div>
      `;
    document.getElementById("tryAgainDiv").style.display = "block";
    document.getElementById("tryAgainButton").disabled = false;
    return "Error";
  }
}

// Input monitoring function
function setupTracking(survey, questionName) {
  const textboxId = survey.getQuestionByName(questionName).id + "i";
  const setupTextboxEvents = () => {
    const textbox = document.getElementById(textboxId);

    if (!textbox) return; // Return if the textbox is not yet available in the DOM

    // Retrieve previously stored values
    let totalFocusedTime = parseInt(survey.getVariable(`${questionName}_time`), 10) || 0;
    let keystrokeCount = parseInt(survey.getVariable(`${questionName}_keystrokes`), 10) || 0;
    let timerInterval = null;
    let startTime = 0; // Start time when focused

    // Start the timer
    const startTimer = () => {
      if (!timerInterval) {
        startTime = Date.now(); // Record the time when focus starts
        timerInterval = setInterval(() => {
          const elapsedTime = Math.floor((Date.now() - startTime) / 1000);
          survey.setVariable(`${questionName}_time`, totalFocusedTime + elapsedTime);
        }, 1000); // Update every second
      }
    };

    // Stop the timer and update the total time
    const stopTimer = () => {
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
        totalFocusedTime += Math.floor((Date.now() - startTime) / 1000); // Add elapsed time to total
        survey.setVariable(`${questionName}_time`, totalFocusedTime);
      }
    };

    // Count keystrokes only when focused
    const countKeystrokes = (event) => {
      if (event.isTrusted && textbox === document.activeElement) { // Ensure the event is a valid user input
        keystrokeCount++;
        survey.setVariable(`${questionName}_keystrokes`, keystrokeCount);
      }
    };

    // Add event listeners for focus, blur, and keystrokes
    textbox.addEventListener("focus", startTimer);
    textbox.addEventListener("blur", stopTimer);
    textbox.addEventListener("keydown", countKeystrokes);
  };

  // Watch for the textbox being added back to the DOM
  const observeDOMChanges = () => {
    const container = document.getElementById("root");

    // MutationObserver to detect when the textbox is added back to the DOM
    const observer = new MutationObserver(() => {
      const textbox = document.getElementById(textboxId);
      if (textbox) {
        setupTextboxEvents(); // Reattach the event listeners once the textbox exists
      }
    });

    // Start observing for DOM changes
    observer.observe(container, { childList: true, subtree: true });

    // Initial setup if the textbox is already in the DOM
    setupTextboxEvents();
  };

  observeDOMChanges(); // Begin observing and setup tracking
}

// {% customFunctions %}

// placeholder

// {% end customFunctions %}

registerCustomFunctions();

function SurveyComponent() {
  const survey = new Model(json);
  survey.participantID = MakeID(8);
  const dateStarted = new Date();

  document.documentElement.lang = survey.locale;
  const completedHtml = survey.completedHtml + "<br>";
  survey.completedHtml = '<div style="text-align: center; padding-bottom: 2em;"><div class="lds-dual-ring"></div></div>';
  document.getElementById("tryAgainButton").innerHTML = SurveyCore.surveyLocalization.getString("saveAgainButton", survey.locale);

  survey.setVariable("group", groupNumber(config.numberOfGroups));
  survey.setVariable("dateStarted", dateStarted.toISOString());

  document.getElementById("tryAgainButton").addEventListener("click", () => {
    if (survey.isCompleted) {
      document.getElementsByClassName("sd-completedpage")[0].innerHTML = '<div style="text-align: center; padding-bottom: 2em;"><div class="lds-dual-ring"></div></div>';
      document.getElementById("tryAgainDiv").style.display = "none";
      document.getElementById("tryAgainButton").disabled = true;
      handleResults(survey, completedHtml)
    }
  });

  survey.onAfterRenderSurvey.add((sender, options) => {
    document.body.style.setProperty("--sjs-general-backcolor-dim", document.getElementsByClassName("sd-root-modern")[0].style.getPropertyValue("--sjs-general-backcolor-dim"));
  });

  // Markdown formatting
  const converter = new Converter();
  survey.onTextMarkdown.add(function (survey, options) {
    // Convert Markdown to HTML
    let str = converter.makeHtml(options.text);
    // Remove root paragraphs <p></p>
    str = str.substring(3);
    str = str.substring(0, str.length - 4);
    // Set HTML markup to render
    options.html = str;
  });

  // Input monitoring setup
  SurveyCore.Serializer.addProperty("question", { name: "monitorInput", type: "boolean" })
  survey.onAfterRenderQuestion.add((sender, options) => {
    if (options.question.getPropertyValue("monitorInput", false)) setupTracking(sender, options.question.name);
  });

  // {% customCode %}

  // placeholder

  // {% end customCode %}

  survey.onComplete.add(sender => handleResults(sender, completedHtml));
  return <Survey model={survey} />;
}

export default SurveyComponent;
