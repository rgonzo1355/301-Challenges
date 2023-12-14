# Import the Active Directory module
Import-Module ActiveDirectory

# Prompt for user details
$UserFullName = Read-Host "Enter the full name of the new AD user"
$UserTitle = Read-Host "Enter the title for the new AD user"

# Generate username by removing spaces from full name
$UserName = $UserFullName -replace ' ', ''

# Check if the user already exists
if (Get-ADUser -Filter "SamAccountName -eq '$UserName'") {
    Write-Host "User $UserName already exists in AD."
    return
}

# Define the list of possible OUs
$OUs = @(
    "Builtin",
    "Computer",
    "Domain Controllers",
    "Finance",
    "Ghost Unit",
    "HR",
    "IT Managed Service Accounts",
    "Sales Department",
    "Users",
    "TPS"
)

# Display the list of OUs with numbers
Write-Host "Choose the OU for the new user:"
for ($i = 0; $i -lt $OUs.Count; $i++) {
    Write-Host "$($i+1). $($OUs[$i])"
}

# Prompt the user to select an OU by number
$OUChoice = Read-Host "Enter the number of the OU for the new user"
$OUChoice = [int]$OUChoice

# Validate the user's choice
if ($OUChoice -ge 1 -and $OUChoice -le $OUs.Count) {
    $SelectedOU = $OUs[$OUChoice - 1]
    $Password = "Password12345"
    $SecPassword = ConvertTo-SecureString $Password -AsPlainText -Force
    $UserPrincipalName = "$UserName@corp.globexpower.com"

    # Construct the Distinguished Name (DN) of the selected OU
    $OUDN = "OU=$SelectedOU,DC=corp,DC=globexpower,DC=com"

    # Create the new user
    try {
        New-ADUser -Name $UserName -SamAccountName $UserName -UserPrincipalName $UserPrincipalName -AccountPassword $SecPassword -Enabled $true -Path $OUDN -ChangePasswordAtLogon $true -Title $UserTitle
        Write-Host "Account Creation Successful. Username: $UserName, Password: $Password"
    } catch {
        Write-Host "An error occurred: $_"
    }
} else {
    Write-Host "Invalid choice. Please enter a valid number for the OU."
}
