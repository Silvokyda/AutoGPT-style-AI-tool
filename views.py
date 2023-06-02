# views.py

from django.shortcuts import render
from django.http import HttpResponse
import openai
import json

# Set up OpenAI API credentials
openai.api_key = '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'


def generate_vulnerable_code(request):
    if request.method == 'POST':
        # Retrieve user inputs from the form
        language = request.POST.get('language')
        vulnerability = request.POST.get('vulnerability')
        feature = request.POST.get('feature')

        # Generate code snippets and vulnerability details using OpenAI
        response = openai.Completion.create(
            engine="code-davinci-001",
            prompt=f'Language: {language}\nVulnerability: {vulnerability}\nFeature: {feature}',
            n=1,
            stop=None,
            temperature=0,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        if response['choices'][0]['text']:
            generated_code = response['choices'][0]['text']
            vulnerability_details = extract_vulnerability_details(
                generated_code)

            # Integrate the generated code into the appropriate Django files
            integrate_code(generated_code)

            # Generate the JSON file with vulnerability details
            generate_vulnerability_json(vulnerability_details)

            # Generate the solution markdown file
            generate_solution_markdown(vulnerability_details)

            # You can replace this with a success page or redirect the user to the generated code page
            return HttpResponse("Code generation successful!")
        else:
            # You can handle the error case appropriately
            return HttpResponse("Error occurred during code generation.")

    # Render the initial form page
    return render(request, 'generate.html')
