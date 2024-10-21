                        PRACTICAL NO.03

3. Working with Web Forms and Controls 

a. Create a simple web page with various sever controls to demonstrate setting and use of 
their properties. (Example : AutoPostBack) 

CODE:
ASPX CODE:
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication5.WebForm1" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Demo</title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Label1" runat="server" BorderStyle="Ridge" Font-Bold="True" Font-Size="X-Large" style="z-index: 1; left: 496px; top: 15px; position: absolute; width: 245px" Text="Registration Form"></asp:Label>
        </div>
        <asp:Label ID="Label2" runat="server" Font-Bold="True" Font-Size="Large" style="z-index: 1; left: 402px; top: 138px; position: absolute; width: 149px" Text="Username :"></asp:Label>
        <asp:TextBox ID="uname" runat="server" BorderStyle="Solid" OnTextChanged="TextBox1_TextChanged" style="z-index: 1; left: 570px; top: 140px; position: absolute; width: 186px; height: 27px" AutoPostBack="True"></asp:TextBox>
        <asp:Label ID="Label3" runat="server" Font-Bold="True" Font-Size="Large" style="z-index: 1; left: 410px; top: 225px; position: absolute; width: 88px" Text="Age :"></asp:Label>
        <asp:TextBox ID="age" runat="server" AutoPostBack="True" BorderStyle="Solid" OnTextChanged="age_TextChanged" style="z-index: 1; left: 568px; top: 223px; position: absolute; width: 199px; height: 26px"></asp:TextBox>
        <asp:Label ID="Label4" runat="server" Font-Bold="True" Font-Size="Large" style="z-index: 1; left: 403px; top: 302px; position: absolute; width: 115px; height: 24px" Text="Gender :"></asp:Label>
        <asp:RadioButtonList ID="rbt" runat="server" AutoPostBack="True" BorderStyle="Ridge" OnSelectedIndexChanged="rbt_SelectedIndexChanged" RepeatDirection="Horizontal" style="z-index: 1; left: 572px; top: 298px; position: absolute; height: 28px; width: 340px">
            <asp:ListItem Value="1">Male</asp:ListItem>
            <asp:ListItem Value="2">Female</asp:ListItem>
            <asp:ListItem Value="3">Other</asp:ListItem>
        </asp:RadioButtonList>
<asp:Label ID="Label5" runat="server" Font-Bold="True" Font-Size="Large" style="z-index: 1; left: 406px; top: 373px; position: absolute; width: 101px" Text="Hobbies :"></asp:Label>
        <asp:DropDownList ID="ddl" runat="server" AutoPostBack="True" Font-Bold="True" Font-Italic="False" Font-Size="Large" style="z-index: 1; left: 576px; top: 368px; position: absolute; height: 33px; width: 238px" OnSelectedIndexChanged="ddl_SelectedIndexChanged">
            <asp:ListItem Value="1">Swiming</asp:ListItem>
            <asp:ListItem Value="2">Writing</asp:ListItem>
            <asp:ListItem Value="3">Reading</asp:ListItem>
            <asp:ListItem Value="4">None</asp:ListItem>
            <asp:ListItem></asp:ListItem>
        </asp:DropDownList>
        <asp:Label ID="Label6" runat="server" Font-Bold="True" Font-Size="Large" style="z-index: 1; left: 405px; top: 454px; position: absolute; width: 120px" Text="Mobile No :"></asp:Label>
        <asp:TextBox ID="mno" runat="server" AutoPostBack="True" BorderStyle="Solid" Font-Bold="True" MaxLength="10" OnTextChanged="TextBox3_TextChanged" Rows="1" style="z-index: 1; left: 582px; top: 448px; position: absolute; height: 26px; width: 202px" TextMode="Number"></asp:TextBox>
        <asp:TextBox ID="pass" runat="server" AutoPostBack="True" BorderStyle="Solid" OnTextChanged="TextBox4_TextChanged" style="z-index: 1; left: 577px; top: 531px; position: absolute; width: 207px; height: 26px" TextMode="Password"></asp:TextBox>
        <asp:Label ID="Label7" runat="server" Font-Bold="True" Font-Size="Large" style="z-index: 1; top: 533px; position: absolute; right: 879px; width: 125px" Text="Password :"></asp:Label>
        <asp:Button ID="submit" runat="server" BorderStyle="Groove" Font-Bold="True" Font-Size="Large" OnClick="Button1_Click" style="z-index: 1; left: 588px; top: 640px; position: absolute; width: 171px" Text="Button" />
        <asp:Label ID="show" runat="server" BorderStyle="None" Font-Bold="True" Font-Size="Large" style="z-index: 1; left: 426px; top: 712px; position: absolute; width: 432px; height: 36px"></asp:Label>
    </form>
</body>
</html>

C# CODE:
using System;
using System.Collections.Generic;

namespace WebApplication5
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            show.Text = "Username :"+uname.Text + "<br/>" + "Age :" + age.Text + 
                "<br/>" + "Gender :" + rbt.SelectedItem + "<br/>" +
                "Hobbies :" + ddl.SelectedItem + "<br/>" +"MobileNo :"+
                mno.Text + "<br/>" + "Password :" + pass.Text;
        }
    }
}
OUTPUT:
















b. Demonstrate the use of Calendar control to perform following operations. 
a) Display messages in a calendar control
b) Display vacation in a calendar control 
c) Selected day in a calendar control using style 
d) Difference between two calendar dates

CODE:
ASPX CODE:
//Name:Rohit Laxman Ghadi
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm2.aspx.cs" Inherits="WebApplication5.WebForm2" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Label1" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Overline="False" Font-Size="Larger" style="z-index: 1; left: 519px; top: 25px; position: absolute; width: 253px; height: 35px" Text="Calendar Controls"></asp:Label>
        </div>
        <asp:Calendar ID="Calendar1" runat="server" BackColor="White" BorderColor="Black" BorderStyle="Solid" CellSpacing="1" Font-Names="Verdana" Font-Size="9pt" ForeColor="Black" NextPrevFormat="ShortMonth" OnDayRender="Calendar1_DayRender" OnSelectionChanged="Calendar1_SelectionChanged" style="z-index: 1; left: 286px; top: 135px; position: absolute; height: 261px; width: 413px">
            <DayHeaderStyle Font-Bold="True" Font-Size="8pt" ForeColor="#333333" Height="8pt" />
            <DayStyle BackColor="#CCCCCC" />
            <NextPrevStyle Font-Bold="True" Font-Size="8pt" ForeColor="White" />
            <OtherMonthDayStyle ForeColor="#999999" />
            <SelectedDayStyle BackColor="#333399" ForeColor="White" />
            <TitleStyle BackColor="#333399" BorderStyle="Solid" Font-Bold="True" Font-Size="12pt" ForeColor="White" Height="12pt" />
            <TodayDayStyle BackColor="#999999" ForeColor="White" />
        </asp:Calendar>
        <asp:Label ID="show" runat="server" Font-Bold="True" Font-Size="Large" style="z-index: 1; left: 402px; top: 463px; position: absolute; width: 395px; height: 48px"></asp:Label>
        <asp:Label ID="show2" runat="server" Font-Bold="True" Font-Size="Large" style="position: absolute; z-index: 1; left: 405px; top: 522px; width: 391px; height: 43px"></asp:Label>
        <asp:Calendar ID="Calendar2" runat="server" BackColor="White" BorderColor="Black" BorderStyle="Solid" CellSpacing="1" Font-Names="Verdana" Font-Size="9pt" ForeColor="Black" NextPrevFormat="ShortMonth" OnSelectionChanged="Calendar2_SelectionChanged" style="z-index: 1; left: 763px; top: 134px; position: absolute; height: 262px; width: 426px">
            <DayHeaderStyle Font-Bold="True" Font-Size="8pt" ForeColor="#333333" Height="8pt" />
            <DayStyle BackColor="#CCCCCC" />
            <NextPrevStyle Font-Bold="True" Font-Size="8pt" ForeColor="White" />
            <OtherMonthDayStyle ForeColor="#999999" />
            <SelectedDayStyle BackColor="#333399" ForeColor="White" />
            <TitleStyle BackColor="#333399" BorderStyle="Solid" Font-Bold="True" Font-Size="12pt" ForeColor="White" Height="12pt" />
            <TodayDayStyle BackColor="#999999" ForeColor="White" />
        </asp:Calendar>
        <asp:Button ID="Button1" runat="server" BorderStyle="Groove" Font-Bold="True" Font-Italic="False" Font-Size="Large" OnClick="Button1_Click" style="z-index: 1; left: 512px; top: 583px; position: absolute; width: 270px" Text="Calculate Difference" />
    </form>
</body>
</html>

C# CODE:
using System;
using System.Collections.Generic;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication5
{
    public partial class WebForm2 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void Calendar1_DayRender(object sender, DayRenderEventArgs e)
        {
            if (e.Day.Date.Year == 2024 && e.Day.Date.Month == 10 && 
e.Day.Date.Day == 31)
            {
                Label l = new Label();
                l.Text = "<br/>Happy<br/>Birthday";
                e.Cell.Controls.Add(l);
            }
            if (e.Day.Date.Year == 2024 && e.Day.Date.Month == 12 && 
e.Day.Date.Day == 25)
            {
                Label l = new Label();
                l.Text = "<br/>Christmas<br/>Vacation";
                Calendar1.SelectedDate = new DateTime(2024, 12, 25);
                Calendar1.SelectedDates.SelectRange(Calendar1.SelectedDate, Calendar1.SelectedDate.AddDays(6));
                e.Cell.Controls.Add(l);
            }
        }

        protected void Calendar1_SelectionChanged(object sender, EventArgs e)
        {
            DateTime seldate = Calendar1.SelectedDate;
            string sday = seldate.DayOfWeek.ToString();
            show.Text = "Selected Day is : " + sday;

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            TimeSpan d1 = Calendar1.SelectedDate - Calendar2.SelectedDate;
            show2.Text = "Difference Between Two Selected date is : 				"+(Math.Abs(d1.TotalDays).ToString());
        }
       protected void Calendar2_SelectionChanged(object sender, EventArgs e)
        {

        }
    }
}
OUTPUT:

Display Message :














Display Vacation:


















Display Selected day:















Display Difference between two dates in days:


c. Demonstrate the use of Treeview control perform following operations
a) Treeview control and datalist 
b) Treeview operations

CODE:
ASPX CODE:
//Name:Rohit Laxman Ghadi
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm3.aspx.cs" Inherits="WebApplication5.WebForm3" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Label1" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Size="Larger" style="z-index: 1; left: 344px; top: 34px; position: absolute; width: 448px; height: 36px" Text="Tree View Control and Operations"></asp:Label>
        </div>
        <asp:TreeView ID="TreeView1" runat="server" ImageSet="XPFileExplorer" NodeIndent="15" style="z-index: 1; left: 483px; top: 113px; position: absolute; height: 67px; width: 390px; bottom: 499px" OnSelectedNodeChanged="TreeView1_SelectedNodeChanged" OnTreeNodeCollapsed="TreeView1_TreeNodeCollapsed">
            <HoverNodeStyle BorderStyle="None" Font-Bold="True" Font-Italic="False" Font-Size="Large" Font-Underline="True" ForeColor="#6666AA" />
            <Nodes>
                <asp:TreeNode Text="College" Value="Department" Checked="True" ShowCheckBox="True">
                    <asp:TreeNode Text="IT Department" Value="IT" Checked="True" ShowCheckBox="True">
                        <asp:TreeNode Text="FYIT" Value="FYIT" Checked="True" ShowCheckBox="True"></asp:TreeNode>
                        <asp:TreeNode Text="SYIT" Value="SYIT" Checked="True" ShowCheckBox="True"></asp:TreeNode>
                        <asp:TreeNode Text="TYIT" Value="TYIT" Checked="True" ShowCheckBox="True"></asp:TreeNode>
                    </asp:TreeNode>
                    <asp:TreeNode Text="CS Department" Value="CS" Checked="True" ShowCheckBox="True">
                        <asp:TreeNode Text="FYCS" Value="FYCS" Checked="True" ShowCheckBox="True"></asp:TreeNode>
                        <asp:TreeNode Text="SYCS" Value="SYCS" Checked="True" ShowCheckBox="True"></asp:TreeNode>
                        <asp:TreeNode Text="TYCS" Value="TYCS" Checked="True" ShowCheckBox="True"></asp:TreeNode>
                    </asp:TreeNode>
                </asp:TreeNode>
            </Nodes>
            <NodeStyle Font-Names="Tahoma" Font-Size="8pt" ForeColor="Black" HorizontalPadding="2px" NodeSpacing="0px" VerticalPadding="2px" />
            <ParentNodeStyle Font-Bold="False" />
            <SelectedNodeStyle BackColor="#B5B5B5" Font-Underline="False" HorizontalPadding="0px" VerticalPadding="0px" />
        </asp:TreeView>
       

        <asp:DataList ID="DataList1" runat="server" OnSelectedIndexChanged="DataList1_SelectedIndexChanged1" style="z-index: 1; left: 338px; top: 395px; position: absolute; height: 78px; width: 476px">
        <ItemTemplate>
            <%# Eval("text")  %>
        </ItemTemplate>
        </asp:DataList>
        <p>
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" style="z-index: 1; left: 522px; top: 628px; position: absolute; width: 229px; height: 42px" Text="Button" />
        </p>
    </form>
</body>
</html>

C#Code:
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication5
{
    public partial class WebForm3 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void DataList1_SelectedIndexChanged1(object sender, EventArgs e)
        {
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            TreeNodeCollection T;
            T = TreeView1.CheckedNodes;
            DataList1.DataSource = T;
            DataList1.DataBind();
            DataList1.Visible = true;
       }

        protected void TreeView1_SelectedNodeChanged(object sender, EventArgs e)
        {
           Response.Write("You Selected Following : " + TreeView1.SelectedValue);

        }

        protected void TreeView1_TreeNodeCollapsed(object sender, TreeNodeEventArgs e)
        {
            Response.Write("The Value Collapsed Was : " + e.Node.Value);
        }
    }
}

OUTPUT:
Treeview Operations:
1]Collapse:



2]Selected:










Treeview control and datalist:


























