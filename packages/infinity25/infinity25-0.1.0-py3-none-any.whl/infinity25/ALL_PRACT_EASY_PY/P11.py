PRACTICAL NO.11

Write the program for the following: 
a. Create a web application to demonstrate use of GridView button column and GridView events  along with paging and sorting.
CODE:
ASPX CODE:

<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm2.aspx.cs" Inherits="WebApplication8.WebForm2" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            position: absolute;
            top: 24px;
            left: 322px;
            z-index: 1;
        }
        .auto-style3 {
            position: absolute;
            top: 432px;
            left: 344px;
            z-index: 1;
            width: 543px;
            height: 38px;
        }
        .auto-style4 {
            width: 82px;
            height: 180px;
            position: absolute;
            top: 110px;
            left: 307px;
            z-index: 1;
            margin-left: 0px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
        <asp:Label ID="Label1" runat="server" BorderStyle="Solid" CssClass="auto-style1" Font-Bold="True" Font-Size="Large" Text="GridView Column Button With Paging and Sorting"></asp:Label>
        <asp:Label ID="Label2" runat="server" CssClass="auto-style3" Font-Bold="True" Font-Size="Large"></asp:Label>
        <asp:GridView ID="GridView1" runat="server" AllowPaging="true" AllowSorting="true" BackColor="White" BorderColor="White" BorderStyle="Ridge" BorderWidth="2px" CellPadding="3" CellSpacing="1" CssClass="auto-style4" GridLines="None" OnPageIndexChanging="GridView1_PageIndexChanging" OnRowCommand="GridView1_RowCommand" OnSorting="GridView1_Sorting">
            <Columns>
                <asp:ButtonField ButtonType="Button" CommandName="Show" Text="Show Detail" />
            </Columns>
            <FooterStyle BackColor="#C6C3C6" ForeColor="Black" />
            <HeaderStyle BackColor="#4A3C8C" Font-Bold="True" ForeColor="#E7E7FF" />
            <PagerStyle BackColor="#C6C3C6" ForeColor="Black" HorizontalAlign="Right" />
            <RowStyle BackColor="#DEDFDE" ForeColor="Black" />
            <SelectedRowStyle BackColor="#9471DE" Font-Bold="True" ForeColor="White" />
            <SortedAscendingCellStyle BackColor="#F1F1F1" />
            <SortedAscendingHeaderStyle BackColor="#594B9C" />
            <SortedDescendingCellStyle BackColor="#CAC9C9" />
            <SortedDescendingHeaderStyle BackColor="#33276A" />
        </asp:GridView>
    </form>
</body>
</html>

C# CODE:
using System;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.SqlClient;
namespace WebApplication8
{
    public partial class WebForm2 : System.Web.UI.Page
    {
        SqlConnection con = new SqlConnection(@"Data Source=ROHIT;Initial Catalog=Employee;Integrated Security=True");
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                display();
            }
        }
        public void display()
        {
            con.Open();
            SqlDataAdapter sda = new SqlDataAdapter("select * from Employee",con);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            GridView1.DataSource = dt;
            GridView1.DataBind();
            con.Close();
            ViewState["dt"] = dt;
            ViewState["sort"] = "ASC";
        }
        protected void GridView1_RowCommand(object sender, GridViewCommandEventArgs e)
        {
            if(e.CommandName=="Show")
            {
                int index = Convert.ToInt32(e.CommandArgument.ToString());
                GridViewRow row = GridView1.Rows[index];
                String name = row.Cells[2].Text;
                String sal = row.Cells[3].Text;
                Label2.Text = "Selected Employee Name is :" + name + "  and Salary is : " + sal;
            }
        }

        protected void GridView1_PageIndexChanging(object sender, GridViewPageEventArgs e)
        {
            //paging concept 
            GridView1.PageIndex = e.NewPageIndex;
            display();
        }

        protected void GridView1_Sorting(object sender, GridViewSortEventArgs e)
        {
            //sorting concept
            DataTable res = ViewState["dt"] as DataTable;
            if (res!=null && res.Rows.Count > 0 )
            {
                if (ViewState["sort"].ToString() == "DESC")
                {
                    res.DefaultView.Sort = e.SortExpression + " DESC";
                    ViewState["sort"] = "DESC";
                }
                else
                {
                    res.DefaultView.Sort = e.SortExpression + " ASC";
                    ViewState["sort"] = "ASC";
                }
                GridView1.DataSource = res.DefaultView;
                GridView1.DataBind();
            }
        }
    }
}

OUTPUT:

GridView Button: 















Paging:
















Sorting:















b. Create a web application to demonstrate data binding using DetailsView and FormView Control.

CODE:
ASPX CODE:
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm3.aspx.cs" Inherits="WebApplication8.WebForm3" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            position: absolute;
            top: 19px;
            left: 320px;
            z-index: 1;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Label1" runat="server" BorderStyle="Solid" CssClass="auto-style1" Font-Bold="True" Font-Size="Large" Text="Data Binding Using DetailView and FormView"></asp:Label>
          
        </div>
        <br />
        <asp:FormView ID="FormView1" runat="server" AllowPaging="True" DataSourceID="SqlDataSource1">
            <EditItemTemplate>
                Eid:
                <asp:TextBox ID="EidTextBox" runat="server" Text='<%# Bind("Eid") %>' />
                <br />
                Ename:
                <asp:TextBox ID="EnameTextBox" runat="server" Text='<%# Bind("Ename") %>' />
                <br />
                salary:
                <asp:TextBox ID="salaryTextBox" runat="server" Text='<%# Bind("salary") %>' />
                <br />
                Department:
                <asp:TextBox ID="DepartmentTextBox" runat="server" Text='<%# Bind("Department") %>' />
                <br />
                <asp:LinkButton ID="UpdateButton" runat="server" CausesValidation="True" CommandName="Update" Text="Update" />
                &nbsp;<asp:LinkButton ID="UpdateCancelButton" runat="server" CausesValidation="False" CommandName="Cancel" Text="Cancel" />
            </EditItemTemplate>
            <HeaderTemplate>
                Form View
            </HeaderTemplate>
            <InsertItemTemplate>
                Eid:
                <asp:TextBox ID="EidTextBox" runat="server" Text='<%# Bind("Eid") %>' />
                <br />
                Ename:
                <asp:TextBox ID="EnameTextBox" runat="server" Text='<%# Bind("Ename") %>' />
                <br />
                salary:
                <asp:TextBox ID="salaryTextBox" runat="server" Text='<%# Bind("salary") %>' />
                <br />
                Department:
                <asp:TextBox ID="DepartmentTextBox" runat="server" Text='<%# Bind("Department") %>' />
                <br />
                <asp:LinkButton ID="InsertButton" runat="server" CausesValidation="True" CommandName="Insert" Text="Insert" />
                &nbsp;<asp:LinkButton ID="InsertCancelButton" runat="server" CausesValidation="False" CommandName="Cancel" Text="Cancel" />
            </InsertItemTemplate>
            <ItemTemplate>
                Eid:
                <asp:Label ID="EidLabel" runat="server" Text='<%# Bind("Eid") %>' />
                <br />
                Ename:
                <asp:Label ID="EnameLabel" runat="server" Text='<%# Bind("Ename") %>' />
                <br />
                salary:
                <asp:Label ID="salaryLabel" runat="server" Text='<%# Bind("salary") %>' />
                <br />
                Department:
                <asp:Label ID="DepartmentLabel" runat="server" Text='<%# Bind("Department") %>' />
                <br />
            </ItemTemplate>
        </asp:FormView>

        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:EmployeeConnectionString3 %>" SelectCommand="SELECT * FROM [Employee]"></asp:SqlDataSource>
        <asp:DetailsView ID="DetailsView1" runat="server" Height="106px" Width="220px">
            <FooterTemplate>
                Detail View<br />
            </FooterTemplate>
        </asp:DetailsView>

    </form>
</body>
</html>

C# CODE:
using System;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.SqlClient;

namespace WebApplication8
{
    public partial class WebForm3 : System.Web.UI.Page
    {
        SqlConnection con = new SqlConnection(@"Data Source=ROHIT;Initial Catalog=Employee;Integrated Security=True");

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                //form view binded using ui
                DetailViewBind();
                FormViewBind();

            }

        }
        public void DetailViewBind()
        {
            con.Open();
            SqlDataAdapter sda = new SqlDataAdapter("select * from Employee", con);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            DetailsView1.DataSource = dt;
            DetailsView1.DataBind();
            con.Close();
        }
        public void FormViewBind()
        {
           // con.Open();
           // SqlDataAdapter sda = new SqlDataAdapter("select * from Employee where Eid=1;", con);
           // DataTable dt = new DataTable();
           // sda.Fill(dt);
           //FormView1.DataSource = dt;
           //FormView1.DataBind();
           // con.Close();
        }

    }
}



OUTPUT:

