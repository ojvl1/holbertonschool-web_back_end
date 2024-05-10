export default function createReportObject(employeesList) {
    const myObject = {
      allEmployees: employeesList,
      getNumberOfDepartments(allEmployees) {
        const totalDepartments = Object.keys(allEmployees);
        return totalDepartments.length;
      },
    };
    return myObject;
  }
