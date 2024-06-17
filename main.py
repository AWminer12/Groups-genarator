import calculator
import doc_maker

groups = calculator.main()
doc_maker.make_pdf(groups)