CREATE TABLE Participant (
    Participant_ID INT PRIMARY KEY,
    Last_Name CHAR(30) NOT NULL,
    First_Name CHAR(30),
    Address CHAR(35),
    City CHAR(35),
    State CHAR(2),
    Postal_Code CHAR(5),
    Phone CHAR(12),
    Date_of_Birth DATE
);

CREATE TABLE AdventureClass (
    Class_Number INT PRIMARY KEY,
    Class_Description CHAR(200),
    Max_Number_Of_People INT,
    Class_Fee DECIMAL(10,2)
);

CREATE TABLE Participant_Class_Attendance (
    Participant_ID INT,
    ClassID INT,
    Class_Number INT,
    Class_Date DATETIME,
    Class_Description CHAR(100),
    Last_Name CHAR(30),
    First_Name CHAR(30),
    PRIMARY KEY (Class_Date, Class_Number, Participant_ID),
    FOREIGN KEY (Participant_ID) REFERENCES Participant(Participant_ID),
    FOREIGN KEY (Class_Number) REFERENCES AdventureClass(Class_Number)
);

CREATE TABLE Class_Attendance (
    ClassID INT,
    Participant_ID INT,
    Class_Description CHAR(100),
    Class_Date DATETIME,
    PRIMARY KEY (Participant_ID, ClassID),
    FOREIGN KEY (Participant_ID) REFERENCES Participant(Participant_ID),
    FOREIGN KEY (ClassID) REFERENCES AdventureClass(Class_Number)
);

CREATE TABLE Instructor (
    InstructorID INT PRIMARY KEY,
    I_LastName CHAR(25),
    I_FirstName CHAR(25),
    ClassID INT
);