function student_tab() {
    document.getElementById("student-search-criteria").style.display = "block";
    document.getElementById("enrollment-search-criteria").style.display = "none";
    document.getElementById("course-search-criteria").style.display = "none";
}
function course_tab() {
    document.getElementById("student-search-criteria").style.display = "none";
    document.getElementById("enrollment-search-criteria").style.display = "none";
    document.getElementById("course-search-criteria").style.display = "block";
}
function enrollment_tab() {
    document.getElementById("enrollment-search-criteria").style.display = "block";
    document.getElementById("student-search-criteria").style.display = "none";
    document.getElementById("course-search-criteria").style.display = "none";
}
function batchexport_tab() {
    // document.getElementById("enrollment-search-criteria").style.display = "none";
    // document.getElementById("student-search-criteria").style.display = "none";
    // document.getElementById("course-search-criteria").style.display = "none";
    document.getElementById("master-container").style.display = "none";
} 
