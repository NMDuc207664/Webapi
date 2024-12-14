use project1;
CREATE TABLE TaiLieuMonHoc (
    IDTaitailieumonhocLieu INT PRIMARY KEY,
    IDLopHoc INT NOT NULL,
    TenTaiLieu VARCHAR(255) NOT NULL,
    Descriptions VARCHAR(800) NULL,
    LoaiTaiLieu VARCHAR(100) NOT NULL,
    Link VARCHAR(255) NULL
);