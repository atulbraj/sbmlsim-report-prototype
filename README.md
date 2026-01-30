# Parameter Optimization Report Template - sbmlsim

**Proof-of-concept Quarto report template for automated parameter optimization reporting in sbmlsim.**

Created for GSoC 2026 Issue [#281](https://github.com/nrnb/GoogleSummerOfCode/issues/281) and sbmlsim Issue [#180](https://github.com/matthiaskoenig/sbmlsim/issues/180).

---

## 🎯 Overview

This prototype demonstrates template-based reporting for systems biology workflows using Quarto. It generates **publication-ready interactive HTML reports** from parameter optimization results.

### ✨ Features

- ✅ **Parameter visualization** - Tables and plots with 95% confidence intervals
- ✅ **Goodness-of-fit analysis** - Predicted vs. true values, residual plots  
- ✅ **Performance metrics** - AIC, RMSE, R², χ² statistics
- ✅ **Training/validation comparison** - Model performance across datasets
- ✅ **Statistical quality metrics** - Comprehensive quality assessment
- ✅ **Reproducibility documentation** - Complete methods, settings, and software versions
- ✅ **Self-contained output** - Single HTML file with all embedded plots and assets
- ✅ **Interactive elements** - Collapsible code blocks, responsive design

---

## 📁 Structure

```
sbmlsim-report-prototype/
├── parameter_optimization_report.qmd  # Main Quarto template
├── load_results.py                    # Data loading utilities  
├── sample_results.json                # Example input data structure
├── parameter_optimization_report.html # Generated report (view this!)
└── README.md                          # This file
```

---

## 🚀 Quick Start

### Prerequisites

**1. Install Quarto:**

```bash
# macOS
brew install quarto

# Or download from: https://quarto.org/docs/get-started/
```

**2. Install Python dependencies:**

```bash
pip install pandas matplotlib seaborn numpy jupyter pyyaml tabulate
```

### Generate Report

```bash
# Clone or download this prototype
cd sbmlsim-report-prototype

# Render the report
quarto render parameter_optimization_report.qmd

# Open the generated HTML
open parameter_optimization_report.html
```

**That's it!** You'll see a fully interactive, publication-ready report.

---

## 📊 What's Included

The generated report contains:

### 1. Executive Summary
- Key metrics at a glance (AIC, RMSE, R²)
- Model and method metadata
- Timestamp and software versions

### 2. Optimized Parameters
- Parameter estimates with 95% confidence intervals (table)
- Visual representation with error bars (plot)
- Units and biological context

### 3. Goodness of Fit
- Predicted vs. true values scatter plot
- Residual analysis with distribution
- R² visualization

### 4. Model Performance
- Training vs. validation RMSE comparison
- Statistical quality metrics (AIC, R², χ²)
- Performance threshold indicators

### 5. Methods & Settings
- Complete optimization configuration
- Convergence criteria and iteration count
- Data sample sizes

### 6. Reproducibility Information
- Software versions
- Command-line reproduction instructions
- Proposed API integration example

---

## 🔧 Input Data Format

The template expects JSON input with this structure:

```json
{
  "metadata": {
    "model_id": "string",
    "timestamp": "ISO8601",
    "method": "string",
    "software": "string"
  },
  "optimization_results": {
    "aic": float,
    "rmse": float,
    "r_squared": float,
    "parameters": [
      {
        "name": "string",
        "value": float,
        "confidence_interval": [lower, upper],
        "unit": "string"
      }
    ],
    "training_rmse": float,
    "validation_rmse": float,
    "iterations": int,
    "convergence_criterion": float
  },
  "goodness_of_fit": {
    "training_points": int,
    "validation_points": int,
    "chi_squared": float,
    "degrees_of_freedom": int
  }
}
```

See [`sample_results.json`](sample_results.json) for a complete example.

---

## 🎨 Customization

### Modify Data

Edit `sample_results.json` to use your own optimization results:

```bash
# Edit the JSON file
nano sample_results.json

# Re-render
quarto render parameter_optimization_report.qmd
```

### Customize Template

The Quarto template is highly customizable:

- **Theme:** Change `theme: cosmo` to `theme: flatly`, `darkly`, `solar`, etc.
- **Code visibility:** Toggle `code-fold: true` to show/hide code blocks
- **Figure sizes:** Adjust `fig-width` and `fig-height`
- **Add sections:** Insert new `## Heading` and ` ```{python} ` code blocks

See [Quarto HTML options](https://quarto.org/docs/reference/formats/html.html) for more.

---

## 🧪 Integration with sbmlsim

### Current sbmlsim Reporting

sbmlsim currently uses Jinja2 templates for HTML/Markdown/LaTeX reports:
- Located in `src/sbmlsim/report/experiment_report.py`
- Templates in `src/sbmlsim/resources/templates/`

### Proposed Integration

**Option 1: Standalone CLI Command**

```bash
# After optimization
sbmlsim report quarto \
    --input results/optimization.json \
    --template parameter_optimization \
    --output reports/optimization.html
```

**Option 2: Python API**

```python
from sbmlsim.reporting import generate_quarto_report

# After optimization
results = optimizer.optimize(model, data)

# Generate interactive HTML report
generate_quarto_report(
    results, 
    template='parameter_optimization',
    output='report.html',
    format='html'
)

# Generate static PDF report (via Typst)
generate_quarto_report(
    results, 
    template='parameter_optimization',
    output='report.pdf',
    format='pdf'
)
```

**Option 3: Result Method**

```python
# After optimization
results = optimizer.optimize(model, data)

# Generate report directly from results
results.to_quarto_report(
    template='parameter_optimization',
    output='report.html'
)
```

### Proposed File Structure

```
src/sbmlsim/
├── report/
│   ├── experiment_report.py       # Existing Jinja2 reports
│   ├── quarto_report.py           # New Quarto report generator
│   └── typst_report.py            # New Typst report generator  
└── resources/
    ├── templates/                  # Existing Jinja2 templates
    └── quarto_templates/           # New Quarto templates
        ├── parameter_optimization.qmd
        ├── sensitivity_analysis.qmd
        ├── simulation_experiment.qmd
        └── literature_review.qmd   # PRISMA diagrams
```

---

## 📈 Next Steps for GSoC Project

Based on Issue #180 requirements, the full GSoC project would include:

### Phase 1: Core Templates (Weeks 1-4)
- [ ] Parameter optimization template (✅ **Done in this prototype**)
- [ ] Sensitivity analysis template (heatmaps, summary tables)
- [ ] Simulation experiment template
- [ ] Model documentation template

### Phase 2: PDF Generation (Weeks 5-6)
- [ ] Typst templates for static PDF reports
- [ ] LaTeX alternative for complex equations
- [ ] Publication-ready formatting

### Phase 3: Integration (Weeks 7-9)
- [ ] Integrate into sbmlsim codebase
- [ ] Python API for report generation
- [ ] CLI commands
- [ ] Pydantic models for result data

### Phase 4: CI/CD & Deployment (Weeks 10-12)
- [ ] GitHub Actions workflows for automated report generation
- [ ] GitHub Pages deployment for web reports
- [ ] Example repositories with CI/CD
- [ ] Documentation and tutorials

---

## 🎓 Related Work

- **GSoC Issue:** [#281 - Automated Reporting for Systems Biology Modeling Workflows](https://github.com/nrnb/GoogleSummerOfCode/issues/281)
- **sbmlsim Issue:** [#180 - Interactive web reports and static PDF reports](https://github.com/matthiaskoenig/sbmlsim/issues/180)
- **sbmlsim Repository:** https://github.com/matthiaskoenig/sbmlsim
- **Quarto:** https://quarto.org
- **Typst:** https://typst.app

---

## 👨‍💻 Author

**Atul B Raj**  
GSoC 2026 Pre-Contribution  
GitHub: [@atulbraj](https://github.com/atulbraj)

Created as a proof-of-concept to demonstrate understanding of the template-based reporting approach described by Dr. Matthias König in Issue #281.

---

## 📝 License

This prototype is provided as-is for demonstration purposes.  
sbmlsim is licensed under MIT - see [LICENSE](https://github.com/matthiaskoenig/sbmlsim/blob/develop/LICENSE).

---

## 🙏 Acknowledgments

- Dr. Matthias König for the detailed project description and clarifications
- NRNB GoogleSummerOfCode for the opportunity
- sbmlsim community for the excellent codebase

---

**Questions or feedback?** Open an issue or reach out via the GSoC Issue #281 discussion!
