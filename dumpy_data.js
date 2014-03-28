

var dummy_data = [
	{"name": "John",  "gender": "M", "experience": 2, 
	"university": "WBUT", "graduation_year": "2011", "skills": ["python", "C#", "java"]},
	{"name": "Sam",  "gender": "M", "experience": 3, 
	"university": "BPUT", "graduation_year": "2010", "skills": ["python", "C++"]},
	{"name": "Gita",  "gender": "F", "experience": 5, 
	"university": "PTU", "graduation_year": "2009", "skills": ["C#", "java"]},
	{"name": "Sona",  "gender": "F", "experience": 2, 
	"university": "WBUT", "graduation_year": "2012", "skills": ["jython", "C#"]},
	{"name": "Ramesh",  "gender": "M", "experience": 6, 
	"university": "BHU", "graduation_year": "2012", "skills": ["C#", 'javascript']},
	{"name": "Maria",  "gender": "F", "experience": 1, 
	"university": "WBUT", "graduation_year": "2012", "skills": ["C", "C#"]},
	{"name": "Avishek",  "gender": "M", "experience": 3, 
	"university": "WBUT", "graduation_year": "2012", "skills": ["PHP", "MySql", "jQuery"]},
	{"name": "Sakher",  "gender": "M", "experience": 10, 
	"university": "Christ University", "graduation_year": "2004", "skills": ["Sales", "Marketing"]},
	{"name": "Ali",  "gender": "M", "experience": 5, 
	"university": "Jadavpur University", "graduation_year": "2000", "skills": ["Django", "html", "css", "javascript"]},
	{"name": "Ann",  "gender": "F", "experience": 1, 
	"university": "IIIT", "graduation_year": "2013", "skills": ["java", "jsp"]},
	{"name": "George",  "gender": "M", "experience": 8, 
	"university": "HI Tech", "graduation_year": "2000", "skills": [".Net", "C#"]},
	{"name": "Mark",  "gender": "M", "experience": 9, 
	"university": "WBUT", "graduation_year": "2003", "skills": ["Coldfusion", "Bootstrap"]},
	{"name": "Kiran",  "gender": "F", "experience": 3, 
	"university": "WBUT", "graduation_year": "2011", "skills": ["Python", "Objective C"]},
	{"name": "Tanmaya",  "gender": "M", "experience": 1, 
	"university": "BPUT", "graduation_year": "2012", "skills": ["PHP", "CodeIgnitor"]}
];


for (var i in dummy_data) {
	db.resume_resume.insert(dummy_data[i])
}