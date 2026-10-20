<!--
author:   name last_name
email:    trainingandconferences@vib.be
version:  2.0.0
language: en
narrator: UK English Female

icon:     https://vib.be/sites/vib.sites.vib.be/files/logo_VIB_noTagline.svg

comment:  This document shall provide an entire compendium and course on the
          development of Open-courSes with [LiaScript](https://LiaScript.github.io).
          As the language and the systems grows, also this document will be updated.
          Feel free to fork or copy it, translations are very welcome...

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js
          https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css
link:     https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css
link:     https://raw.githubusercontent.com/vib-tcp/material-liascript/master/img/org.css
link:     https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css
link:     https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@300&display=swap
link:     https://fonts.googleapis.com/css2?family=Open+Sans&display=swap

link:  https://raw.githubusercontent.com/vib-tcp/material-liascript/master/vib-styles.css

@edition:  1st 
@CourseTitle: Bioimaging data analysis: from zero to machine learning hero

import:   https://raw.githubusercontent.com/vib-tcp/training_material_template/refs/heads/main/macro.md

-->

# @CourseTitle

<section>

Hello and welcome to our workshop! We are very happy to have you here.

This is the @edition edition of this workshop, jointly organised by the RACE project.

> We are using the interactive Open Educational Resource online/offline course infrastructure called LiaScript.
> It is a distributed way of creating and sharing educational content hosted on github.
> To see this document as an interactive LiaScript rendered version, click on the
> following link/badge: [LiaScript](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-training-conferences/bioimaging-data-analysis-zero-machine-learning-hero/main/README.md)

## General context

Bioimaging Data Analysis: From Zero to Machine Learning Hero is a three‑day, project‑style course that guides participants through the full journey of understanding, exploring, and analyzing bioimaging data. Beginning with common pitfalls in image acquisition and an accessible introduction to machine learning, participants progressively build practical skills using powerful open‑source tools. Hands‑on sessions with Napari, QuPath, ilastik, and Cellpose provide an interactive foundation for image visualization, segmentation, and quantitative analysis, while lunch‑and‑learn moments introduce broader concepts such as emerging machine‑learning approaches and the Bioimaging Model Zoo.

In the final stretch, participants dive into state‑of‑the‑art deep‑learning tools, including SAM, Empanada, and Napari‑based neural network workflows, before shifting perspective toward responsible and reproducible science. Day three focuses on image ethics, FAIR data principles, and personalized project work in a “Bring Your Own Data” session—allowing each participant to apply new skills directly to their own research questions and leave the course with practical, actionable experience.

This is an event organized as 'RACE event', work package 3 of the RACE project funded by the European Union under Horizon Europe (Project no 101059801). 

Read more about RACE at https://www.iimcb.gov.pl/en/race/

## Proposed Schedule

Schedule day 1:

- 9:00 - 09:20 - Welcome and short introduction of instructors and participants
- 9:30 - 10:30 - Pitfall of the acquisition
- 10:30 - 11:00 - tea and coffee break
- 11:00 - 12:30 - What has machine learning ever done for us
- 12:45 - 13:45 - lunch
- 13:45 - 15:15 - Napari Introduction
- 15:15 - 15:30 - tea and coffee break
- 15:30 - 17:00 - Napari Part II

Schedule day 2:

- 9:00 - 10:30 - Napari Part III
- 11:00 - 11:15 - tea and coffee break
- 11:15 - 12:30 - QuPath - pixel classifier/ object classifiers (a fast intro)
- 12:45 - 13:30 - lunch
- 13:30 - 15:05 - Ilastik - towards machine learning 
- 15:15 - 15:30 - tea and coffee break
- 15:30 - 17:00 - FAIR Imaging resources and image ethics (publications)

Schedule day 3:

- 9:30 - 10:30 - Deep learning with Napari : Noise2Void/Micro-SAM/NNInteractive/Empanada
- 10:30 - 11:05 - tea and coffee break
- 11:15 - 12:45 - Bring your own data (present your challenges
- 12:30 - 13:30 - lunch
- 13:45 - 16:15 - Bring your own data (working on the examples with experts)

</section>

# Lesson overview

> <i class="fa fa-lock"></i> **License:** [Creative Commons Attribution 4.0 International  License](https://creativecommons.org/licenses/by/4.0/deed.en)
>
> <i class="fa fa-user"></i> **Target Audience:** Researchers
>
> <svg xmlns="http://www.w3.org/2000/svg" height="14" width="16" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc.--><path d="M384 64c0-17.7 14.3-32 32-32H544c17.7 0 32 14.3 32 32s-14.3 32-32 32H448v96c0 17.7-14.3 32-32 32H320v96c0 17.7-14.3 32-32 32H192v96c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32h96V320c0-17.7 14.3-32 32-32h96V192c0-17.7 14.3-32 32-32h96V64z"/></svg> **Level:** Beginner  
>
> <i class="fa fa-arrow-left"></i> **Prerequisites**  
> To be able to follow this course, learners should have knowledge in:
> 
> 1. Fundamental understanding of microscopy data. 
> 2. Students should know the essentials of how biological images are acquired (e.g., channels, resolution, noise, file formats) to make sense of topics such as acquisition pitfalls, segmentation workflows, and model performance.
>
> <i class="fa fa-bookmark"></i> **Description**  Bioimaging Data Analysis: From Zero to Machine Learning Hero is a three‑day, project‑style course that guides participants through the full journey of understanding, exploring, and analyzing bioimaging data. Beginning with common pitfalls in image acquisition and an accessible introduction to machine learning, participants progressively build practical skills using powerful open‑source tools. Hands‑on sessions with Napari, QuPath, ilastik, and Cellpose provide an interactive foundation for image visualization, segmentation, and quantitative analysis, while lunch‑and‑learn moments introduce broader concepts such as emerging machine‑learning approaches and the Bioimaging Model Zoo. In the final stretch, participants dive into state‑of‑the‑art deep‑learning tools, including SAM, Empanada, and Napari‑based neural network workflows, before shifting perspective toward responsible and reproducible science. Day three focuses on image ethics, FAIR data principles, and personalized project work in a “Bring Your Own Data” session—allowing each participant to apply new skills directly to their own research questions and leave the course with practical, actionable experience.
> 
> <i class="fa fa-arrow-right"></i> **Learning Outcomes:**  
> By the end of the course, learners will be able to:
>
> 1. Explain common pitfalls in bioimage acquisition and evaluate how they affect downstream analysis quality. 
> 2. Operate core functionalities of Napari, QuPath, ilastik, and Cellpose to visualize, segment, and quantify biological images in a reproducible manner.
> 3. Compare classical image‑analysis approaches with machine‑learning–based workflows, selecting appropriate methods for different bioimaging tasks.
> 4. Apply pixel‑ and object‑classification workflows in QuPath and interpret the resulting segmentation outputs for biological relevance.
> 5. Execute deep‑learning‑based segmentation tools such as SAM and Empanada, and assess their performance using appropriate evaluation criteria.
> 6. Discuss best practices in image ethics and apply FAIR data principles when preparing imaging data for sharing, publication, or reuse.
> 7. Design and implement a basic analysis pipeline for their own dataset (“Bring Your Own Data”), demonstrating problem‑solving, tool selection, and critical interpretation of results.
>
>> Check more about [Bloom's taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/) to categorize the levels in educational goals
>
> <i class="fa fa-hourglass"></i> **Time estimation**: 30 hours
>
> <i class="fa fa-asterisk"></i> **Requirements:** The (technical) installation requirements are described in the [installations]() section.
>
> <i class="fa fa-envelope-open-text"></i> **Supporting Materials**:
> 
> 1. [Exercises and solutions](link)
> 2. [Slides](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-tcp/training_material_template/refs/heads/main/supplementary/chapter_01_presentation.md)  
> 
> <i class="fa fa-life-ring"></i> **Acknowledgement**:
>
> * [RACE](https://www.iimcb.gov.pl/en/race/)
> * [VIB](https://www.vib.be/)
> * [IIMCB](https://www.iimcb.gov.pl/en)
> * [IGC Edinburgh](https://www.research.ed.ac.uk/en/organisations/institute-of-genetics-and-cancer-2/)
>
> <i class="fa fa-money-bill"></i> **Funding:** This project has received funding from the RACE project (RACE project funded by the European Union under Horizon Europe Project no 101059801).
>
> <i class="fa fa-anchor"></i> **PURL**:  


# Authors and Contributors

Authors

- @[orcid(Sebastian Munck)](https://orcid.org/0000-0002-5182-5358)
- @[orcid(Laura Murphy)](https://orcid.org/0000-0003-0029-0434)
- @[orcid(Benjamin Pavie)](https://orcid.org/0000-0002-0249-3844)
- @[orcid(Tomasz Wegierski)](https://orcid.org/0000-0003-2635-8580)
- @[orcid(Ann Wheeler)](https://orcid.org/0009-0007-2979-0308)

## Citing this lesson

Please cite as:

  1. training material of Bioimaging data analysis: from zero to machine learning hero, https://zenodo.org/XXXX
                                         |
# About us

*About VIB and VIB Technologies*

VIB is an entrepreneurial non-profit research institute, with a clear focus on groundbreaking strategic basic research in life sciences and operates in close partnership with the five universities in Flanders – Ghent University, KU Leuven, University of Antwerp, Vrije Universiteit Brussel and Hasselt University.

As part of the VIB Technologies, the 12 VIB Core Facilities, provide support in a wide array of research fields and housing specialized scientific equipment for each discipline. Science and technology go hand in hand. New technologies advance science and often accelerate breakthroughs in scientific research. VIB has a visionary approach to science and technology, founded on its ability to identify and foster new innovations in life sciences.

The goal of VIB Technology Training is to up-skill life scientists to excel in the domains of VIB Technologies, Bioinformatics & AI, Software Development, and Research Data Management.

--------------------------------------------

*Editorial team for this course*

Authors: @[orcid(Alexander Botzki)](https://orcid.org/0000-0001-6691-4233), @[orcid(Bruna Piereck)](https://orcid.org/0000-0001-5958-0669)

Technical Editors: Alexander Botzki

License: [![CC BY SA](img/picture003.jpg)](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

```json   @JSONLD
{
  "@context": "https://schema.org/",
  "@type": "LearningResource",
  "@id": "https://elixir-europe-training.github.io/ELIXIR-TrP-TeSS/",
  "http://purl.org/dc/terms/conformsTo": {
    "@type": "CreativeWork",
    "@id": "https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE"
  },
  "description": "TeSS, how can I help you? This is our interactive hands-on course about efficient use of the ELIXIR TeSS platform.",
  "keywords": "FAIR, OPEN, Bioinformatics, Teaching, TeSS",
  "name": "TeSS, how can I help you?",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "educationalLevel": "beginner",
  "competencyRequired": "none",
  "teaches": [
    "search events and material in TeSS via direct and faceted search",
    "add manually and automatically events and material to TeSS",
    "extract events and material from TeSS by using TeSS widgets"
  ],
  "audience": "training providers",
  "inLanguage": "en-US",
  "learningResourceType": [
    "tutorial"
  ],
  "author": [
    {
      "@type": "Person",
      "name": "Bruna Piereck"
    },
    {
      "@type": "Person",
      "name": "Olivier Sand"
    },
    {
      "@type": "Person",
      "name": "Alexander Botzki"
    }
  ],
  "contributor": [
    {
      "@type": "Person",
      "name": "Yasmine Maes"
    },
    {
      "@type": "Person",
      "name": "Finn Bacall"
    },
    {
      "@type": "Person",
      "name": "Munazah Andrabi"
    }
  ]
}
```











