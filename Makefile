# Plots
generate_passing_per_year_plot:
	python -c "from main import generate_passing_per_year_plot; generate_passing_per_year_plot()"

generate_distribution_per_genre_plot:
	python -c "from main import generate_distribution_per_genre_plot; generate_distribution_per_genre_plot()"

generate_grading_distribution_per_genre_plot:
	python -c "from main import generate_grading_distribution_per_genre_plot; generate_grading_distribution_per_genre_plot()"

# Reports
generate_passing_per_year_report:
	python -c "from main import generate_passing_per_year_report; generate_passing_per_year_report()"

generate_grading_distribution_per_year_report:
	python -c "from main import generate_grading_distribution_per_year_report; generate_grading_distribution_per_year_report()"

generate_distribution_per_genre_report:
	python -c "from main import generate_distribution_per_genre_report; generate_distribution_per_genre_report()"

generate_grading_distribution_per_genre_report:
	python -c "from main import generate_grading_distribution_per_genre_report; generate_grading_distribution_per_genre_report()"
